module "healthcheck" {
  source = "./healthcheck"

  environment = var.environment

  sns_topic = module.alerter.alerter_lambda
}