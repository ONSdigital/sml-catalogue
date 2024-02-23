# This rule triggers the healthcheck lambda every minute
resource "aws_cloudwatch_event_rule" "trigger_healthcheck" {
    name                = "${var.domain_name_base}-healthcheck-trigger"
    description         = "Fires the healthcheck lambda function every minute"
    schedule_expression = "rate(1 minute)"
}

# Points to the healthcheck lambda
resource "aws_cloudwatch_event_target" "sml_site_trigger_healthcheck" {
    rule      = "${aws_cloudwatch_event_rule.trigger_healthcheck.name}"
    target_id = "check_sml_site"
    arn       = "${aws_lambda_function.healthcheck.arn}"
    input     = jsonencode({
                  "site"            : "https://${var.domain_name_base}",
                  "env"             : "${var.environment}"
                  "expected_string" : "An open source library for statistical code approved by the ONS"
                })
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

# This attaches the policy needed for logging to the lambda's IAM role. #3
resource "aws_iam_role_policy_attachment" "lambda_healthcheck" {
  role       = "${aws_iam_role.healthcheck.name}"
  policy_arn = "${aws_iam_policy.lambda_log_function.arn}"
}

# Adds permission for event to invoke healthcheck function
resource "aws_lambda_permission" "allow_event_to_invoke_healthcheck" {
    statement_id  = "AlarmAction"
    action        = "lambda:InvokeFunction"
    function_name = "${aws_lambda_function.healthcheck.function_name}"
    principal     = "events.amazonaws.com"
    source_arn    = "${aws_cloudwatch_metric_alarm.healthcheck.arn}"
}

# Adds permission for cloudwatch to invoke alerter function
resource "aws_lambda_permission" "allow_cloudwatch_to_invoke_alerter" {
    statement_id  = "AlarmAction"
    action        = "lambda:InvokeFunction"
    function_name = "${aws_lambda_function.alerter.function_name}"
    principal     = "lambda.alarms.cloudwatch.amazonaws.com"
    source_arn    = "${aws_cloudwatch_metric_alarm.healthcheck.arn}"
}

# zip healthcheck lambda for deployment to aws
data "archive_file" "zip_the_python_healthcheck_lambda" {
type        = "zip"
source_file = "./healthcheck/lambda_functions/healthcheck/healthcheck.py"
output_path = "./healthcheck/lambda_functions/healthcheck/healthcheck.zip"
}

# zip alerter lambda for deployment to aws
data "archive_file" "zip_the_python_alerter_lambda" {
type        = "zip"
source_file = "./healthcheck/lambda_functions/alerter/alerter.py"
output_path = "./healthcheck/lambda_functions/alerter/alerter.zip"
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

resource "aws_iam_role" "healthcheck" {
  name               = "${var.environment}-healthcheck"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

resource "aws_iam_role" "alerter" {
  name               = "${var.environment}-alerter"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

# creates healthcheck lambda
resource "aws_lambda_function" "healthcheck" {
  role          = aws_iam_role.healthcheck.arn

  function_name = "${var.environment}-healthcheck"

  filename      = "./healthcheck/lambda_functions/healthcheck/healthcheck.zip"

  handler       = "healthcheck.lambda_handler"

  runtime       = "python3.7"
  timeout       = 10
  memory_size   = 512

  tags = {
    Name = "${var.environment}_sml_lambda_health_check"
  }

  environment {
    variables = {
      "expected_string" = "An open source library for statistical code approved by the ONS",
      "env" = var.environment,
      "site" = var.domain_name_base,
    }
  }

}

# creates alerter lambda
resource "aws_lambda_function" "alerter" {
  role          = aws_iam_role.alerter.arn

  function_name = "${var.environment}-alerter"

  filename      = "./healthcheck/lambda_functions/alerter/alerter.zip"

  handler       = "alerter.lambda_handler"

  runtime       = "python3.7"
  timeout       = 10
  memory_size   = 512

  environment {
    variables = {
      "alarm_name" = "${var.environment}-environment-alarm",
      "lambda_name" = "${var.environment}-healthcheck",
      "url" = var.domain_name_base,
      "slack_webhook_url" = "https://hooks.slack.com/triggers/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"
    }
  }

  tags = {
    Name = "${var.environment}_sml_lambda_alerter"
  }

}

# creates route53 and its dependency on cloudwatch alarms
resource "aws_route53_health_check" "sml" {
  type                            = "CLOUDWATCH_METRIC"
  cloudwatch_alarm_name           = aws_cloudwatch_metric_alarm.healthcheck.alarm_name
  cloudwatch_alarm_region         = "eu-west-2"
  insufficient_data_health_status = "Healthy"

  tags = {
    Name = "${var.environment}_environment"
  }

  depends_on                      = [aws_cloudwatch_metric_alarm.healthcheck]
}

# creates the cloudwatch alarm and its dependency on the healthcheck
resource "aws_cloudwatch_metric_alarm" "healthcheck" {
  alarm_name          = "${var.environment}-environment-alarm"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  metric_name         = "Errors"
  namespace           = "AWS/Lambda"
  period              = 300
  statistic           = "Sum"
  threshold           = 3
  alarm_description   = "Alarm for ${var.domain_name_base} has been triggered"
  actions_enabled     = "true"
  alarm_actions       = [aws_sns_topic.sns_topic.arn, aws_lambda_function.alerter.arn]
  treat_missing_data  = "breaching"

  dimensions = {
    FunctionName = aws_lambda_function.healthcheck.function_name
  }

  depends_on          = [aws_lambda_function.healthcheck]
}

# creates and name the sns topic
resource "aws_sns_topic" "sns_topic" {
  name     = "smlPortalTopic"
}

# assigns the team email to the sns topic as a subscription
resource "aws_sns_topic_subscription" "email_target" {
  topic_arn = aws_sns_topic.sns_topic.arn

  protocol  = "email"
  endpoint  = "SMLAdmin@ons.gov.uk"
}

