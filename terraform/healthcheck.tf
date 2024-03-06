module "healthcheck" {
  source = "./healthcheck"

  environment = var.environment

  alerter = module.alerter.alerter_lambda
}