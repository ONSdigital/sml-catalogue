# Add required providers
terraform {
  required_providers {
    archive = {
      source = "hashicorp/archive"
      version = "2.4.2"
    }
  }
}

# Creates iam role
resource "aws_iam_role" "healthcheck" {
  name               = "${var.environment}-healthcheck"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

# This attaches the policy needed for logging to the lambda's IAM role.
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

# Creates healthcheck lambda
resource "aws_lambda_function" "healthcheck" {
  role          = aws_iam_role.healthcheck.arn

  function_name = "${var.environment}-healthcheck"

  filename      = "../lambda_functions/healthcheck/healthcheck.zip"

  handler       = "healthcheck.lambda_handler"

  runtime       = "python3.9"
  timeout       = 10
  memory_size   = 512

  tags = {
    Name = "${var.environment}_sml_lambda_health_check"
  }

}