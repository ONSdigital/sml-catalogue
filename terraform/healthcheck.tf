module "healthcheck" {
  source = "./healthcheck"

  environment = var.environment

  deployment_role = var.deployment_role

  alerter = module.alerter.output.alerter_lambda
}