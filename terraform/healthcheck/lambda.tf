# Add required providers
terraform {
  required_providers {
    archive = {
      source = "hashicorp/archive"
      version = "2.4.2"
    }
  }
}

# Creates healthcheck lambda
resource "aws_lambda_function" "healthcheck" {
  role          = "${var.deployment_role}"

  function_name = "${var.environment}-healthcheck-${terraform.workspace}"

  filename      = "../lambda_functions/healthcheck/healthcheck.zip"

  handler       = "healthcheck.lambda_handler"

  runtime       = "python3.9"
  timeout       = 10
  memory_size   = 512

  tags = {
    Name = "${var.environment}_sml_lambda_health_check"
  }

}