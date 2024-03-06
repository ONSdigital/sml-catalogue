# Define a variable to store the retrieved secret value
variable "slack_webhook_secret" {
  type = string
}

# Retrieve the secret from AWS Secrets Manager
data "aws_secretsmanager_secret" "my_secret" {
  name = "slack_webhook_sml_portal_alerts" 
}

# Extract the secret value from the retrieved secret
data "aws_secretsmanager_secret_version" "my_secret_version" {
  secret_id = data.aws_secretsmanager_secret.my_secret.id
}

# Assign the secret value to the variable
variable "slack_webhook_secret" {
  default = data.aws_secretsmanager_secret_version.my_secret_version.secret_string
}