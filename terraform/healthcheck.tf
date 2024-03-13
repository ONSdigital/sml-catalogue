module "healthcheck" {
  source = "./healthcheck"

  environment = var.environment

  lambda_name_suffix = var.lambda_name_suffix

  alerter = module.alerter.alerter_lambda
}