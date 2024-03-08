module "alerter" {
  source = "./alerter"

  slack_webhook_token = var.slack_alert_token

  environment = var.environment

  domain_name_base = local.domain_name_base[var.environment]
}