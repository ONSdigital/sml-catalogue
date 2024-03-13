# Add required providers
terraform {
  required_providers {
    archive = {
      source = "hashicorp/archive"
      version = "2.4.2"
    }
  }
}

# Creates alerter lambda
resource "aws_lambda_function" "alerter" {
  role          = "DeploymentRoleSMLPolicy"

  function_name = "${var.environment}-alerter-${terraform.workspace}"

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
      "alarm_name" = "${var.environment}-environment-healthcheck-alarm",
      "lambda_name" = "${var.environment}-alerter-${terraform.workspace}",
      "url" = var.domain_name_base,
      "slack_url" = "${var.slack_url}"
      "slack_webhook_token" = "${var.slack_webhook_token}"
    }
  }

}