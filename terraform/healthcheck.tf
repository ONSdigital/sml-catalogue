module "healthcheck" {
  source = "./healthcheck"

  environment = var.environment

  deployment_role = var.deployment_role

  alerter = "arn:aws:lambda:eu-west-2:${var.aws_account_id}:function:${var.deployment_role}-alerter-${var.terraform.workspace}"
  
}