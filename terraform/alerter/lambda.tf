# Add required providers
terraform {
  required_providers {
    archive = {
      source = "hashicorp/archive"
      version = "2.4.2"
    }
  }
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

# This attaches the policy needed for logging to the lambda's IAM role. #3
resource "aws_iam_role_policy_attachment" "lambda_alerter" {
  role       = "${aws_iam_role.alerter.name}"
  policy_arn = "${aws_iam_policy.lambda_log_function.arn}"
}

# Permissions for lambda to log to a log group
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
}

# This creates the policy needed for a lambda to log.
resource "aws_iam_policy" "lambda_log_function" {
  name   = "lambda-alerter-logs"
  path   = "/"
  policy = "${data.aws_iam_policy_document.lambda_log_function.json}"
}

# Creates iam role
resource "aws_iam_role" "alerter" {
  name               = "${var.environment}-alerter"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

# Creates alerter lambda
resource "aws_lambda_function" "alerter" {
  role          = aws_iam_role.alerter.arn

  function_name = "${var.environment}-alerter"

  filename      = "../lambda_functions/alerter/alerter.zip"

  handler       = "alerter.lambda_handler"

  runtime       = "python3.9"
  timeout       = 10
  memory_size   = 512

  tags = {
    Name = "${var.environment}_sml_lambda_alerter"
  }

  environment {
    variables = {
      "alarm_name" = "${var.environment}-environment-alarm",
      "lambda_name" = "${var.environment}-alerter",
      "url" = var.domain_name_base,
      "slack_url" = "${var.slack_url}"
      "webhook_secret" = "${var.slack_secret}"
    }
  }

}