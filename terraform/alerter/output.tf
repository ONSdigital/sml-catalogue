output "alerter_lambda" {
  value = aws_lambda_function.alerter.arn
}

output "slack_secret" {
  value = data.aws_secretsmanager_secret_version.current.secret_string
}