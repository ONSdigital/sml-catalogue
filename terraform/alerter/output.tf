output "alerter_lambda" {
  value = aws_lambda_function.alerter.arn
}

output "slack_secret" {
  type = string
  default = data.aws_secretsmanager_secret_version.current.secret_string
}