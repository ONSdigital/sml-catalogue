module "healthcheck" {
  source = "./healthcheck"

  environment = var.environment
}

module "alerter" {
  source = "./alerter"

  environment = var.environment

  domain_name_base = local.domain_name_base[var.environment]
}