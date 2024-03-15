module "healthcheck" {
  source = "./healthcheck"
  count  = terraform.workspace == "main" ? 1 : 0

  environment = var.environment

  deployment_role = var.deployment_role
}