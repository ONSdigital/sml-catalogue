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

# Creates iam role
resource "aws_iam_role" "alerter" {
  name               = "${var.environment}-alerter"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

# Creates alerter lambda
resource "aws_lambda_function" "alerter" {
  role          = aws_iam_role.alerter.arn

  function_name = "${var.environment}-alerter"

  filename      = "../../lambda_functions/alerter/alerter.zip"

  handler       = "alerter.lambda_handler"

  runtime       = "python3.9"
  timeout       = 10
  memory_size   = 512

  tags = {
    Name = "${var.environment}_sml_lambda_alerter"
  }

}