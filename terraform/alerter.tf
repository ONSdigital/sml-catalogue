module "alerter" {
  source = "./alerter"

  slack_secret = var.slack_secret

  environment = var.environment

  domain_name_base = local.domain_name_base[var.environment]
}