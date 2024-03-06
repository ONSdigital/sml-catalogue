module "alerter" {
  source = "./alerter"

  environment = var.environment

  domain_name_base = local.domain_name_base[var.environment]
}