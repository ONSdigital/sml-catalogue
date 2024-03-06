module "healthcheck" {
  source = "./healthcheck"

  environment = var.environment

  domain_name_base = local.domain_name_base[var.environment]
}