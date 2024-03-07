variable "domain_name_base" {
  type = string
}

variable "environment" {
  type = string
}

locals {
  slack_url = {
    slack_url_prefix : "https://hooks.slack.com/triggers/E04RP3ZJ3QF/6739592211926/"
  }
}