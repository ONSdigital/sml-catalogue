module "healthcheck" {
  source = "./healthcheck"

  environment = var.environment

  deployment_role = var.deployment_role

  aws_account_id = var.aws_account_id

  terraform_workspace = terraform.workspace

}