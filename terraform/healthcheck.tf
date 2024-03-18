module "healthcheck" {
  source = "./healthcheck"
  count  = terraform.workspace == "main" ? 1 : 0

  environment = var.environment

  deployment_role = var.deployment_role

  alerter = "arn:aws:lambda:eu-west-2:${var.aws_account_id}:function:${var.environment}-alerter-${terraform.workspace}"
  
}