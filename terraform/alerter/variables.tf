variable "domain_name_base" {
  type = string
}

variable "environment" {
  type = string
}

variable "slack_url" = {
  default = "https://hooks.slack.com/triggers/E04RP3ZJ3QF/6739592211926/${env.WEBHOOK_SLACK}"
}