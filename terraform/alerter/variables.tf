variable "domain_name_base" {
  type = string
}

variable "deployment_role" {
  type = string
}

variable "environment" {
  type = string
}

variable "slack_url" {
  type = string
  default = "https://hooks.slack.com/triggers/E04RP3ZJ3QF/6739592211926"
}

variable "slack_webhook_token" {
  type = string
}