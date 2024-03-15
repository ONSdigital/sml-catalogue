module "healthcheck" {
  source = "./healthcheck"

  environment = var.environment

  deployment_role = var.deployment_role

  alerter = module.alerter[0].alerter_lambda
}