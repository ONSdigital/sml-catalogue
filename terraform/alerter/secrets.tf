data "aws_secretsmanager_secret" "secrets" {
  name = "slack_webhook_sml_portal_alerts"
}

data "aws_secretsmanager_secret_version" "current" {
  secret_id = data.aws_secretsmanager_secret.secrets.id
}