module "alerter" {
  source = "./alerter"
  count  = terraform.workspace == "main" ? 1 : 0

  slack_webhook_token = var.slack_alert_token

  environment = var.environment

  deployment_role = var.deployment_role

  domain_name_base = local.domain_name_base[var.environment]
}