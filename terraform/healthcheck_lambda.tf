# This rule triggers the healthcheck lambda every minute
resource "aws_cloudwatch_event_rule" "trigger_healthcheck" {
    name                = "${local.domain_name_base[var.environment]}-healthcheck-trigger"
    description         = "Fires the healthcheck lambda function every minute"
    schedule_expression = "rate(1 minute)"
}

# Points to the healthcheck lambda
resource "aws_cloudwatch_event_target" "sml_site_trigger_healthcheck" {
    rule      = "${aws_cloudwatch_event_rule.trigger_healthcheck.name}"
    target_id = "check_sml_site"
    arn       = "${aws_lambda_function.healthcheck.arn}"
    input     = jsonencode({
                  "site"            : "https://${local.domain_name_base[var.environment]}",
                  "env"             : "${var.environment}",
                  "expected_string" : "An open source library for statistical code approved by the ONS"
                })
}

# Adds permission for event to invoke healthcheck function
resource "aws_lambda_permission" "allow_event_to_invoke_healthcheck" {
    statement_id  = "AlarmAction"
    action        = "lambda:InvokeFunction"
    function_name = "${aws_lambda_function.healthcheck.function_name}"
    principal     = "events.amazonaws.com"
    source_arn    = "${aws_cloudwatch_event_rule.trigger_healthcheck.arn}"
}

# creates iam role
resource "aws_iam_role" "healthcheck" {
  name               = "${var.environment}-healthcheck"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

# This attaches the policy needed for logging to the lambda's IAM role. #3
resource "aws_iam_role_policy_attachment" "lambda_healthcheck" {
  role       = "${aws_iam_role.healthcheck.name}"
  policy_arn = "${aws_iam_policy.lambda_log_function.arn}"
}

# Allow role to be assumed so lambdas can run
data "aws_iam_policy_document" "assume_role" {
  statement {
    effect  = "Allow"
    actions = [
      "sts:AssumeRole",
      ]

    principals {
      identifiers = ["lambda.amazonaws.com"]
      type        = "Service"
    }
  }
}

# Permissions for lambda to log to a log group and for cloudwatch to put metric data
data "aws_iam_policy_document" "lambda_log_function" {
  statement {
    actions = [
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents"
    ]

    resources = [
      "arn:aws:logs:*:*:*",
    ]
  }

  statement {
    actions = [
      "cloudwatch:PutMetricData"
    ]

    resources = [
      "*",
    ]
  }
  
}

# This creates the policy needed for a lambda to log.
resource "aws_iam_policy" "lambda_log_function" {
  name   = "lambda-healthcheck-logs"
  path   = "/"
  policy = "${data.aws_iam_policy_document.lambda_log_function.json}"
}

# zip healthcheck lambda for deployment to aws
data "archive_file" "zip_the_python_healthcheck_lambda" {
type        = "zip"
source_file = "./healthcheck/lambda_functions/healthcheck/healthcheck.py"
output_path = "./healthcheck/lambda_functions/healthcheck/healthcheck.zip"
}

# creates healthcheck lambda
resource "aws_lambda_function" "healthcheck" {
  role          = aws_iam_role.healthcheck.arn

  function_name = "${var.environment}-healthcheck"

  filename      = "./healthcheck/lambda_functions/healthcheck/healthcheck.zip"

  handler       = "healthcheck.lambda_handler"

  runtime       = "python3.9"
  timeout       = 10
  memory_size   = 512

  tags = {
    Name = "${var.environment}_sml_lambda_health_check"
  }

  environment {
    variables = {
      "expected_string" = "An open source library for statistical code approved by the ONS",
      "env" = var.environment,
      "site" = local.domain_name_base[var.environment],
    }
  }

}