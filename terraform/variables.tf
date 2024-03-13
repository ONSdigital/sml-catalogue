resource "lambda_name" "suffix" {
  length = 16
  special = false
}

locals {
  lambda_name_suffix = lambda_name.suffix
}

variable "environment" {
  type = string
}

variable "slack_alert_token" {
  type = string
}

variable "deployment_role" {
  type = string
}

locals {
  domain_name_base = {
    dev : "dev-sml.aws.onsdigital.uk"
    preprod : "preprod-sml.aws.onsdigital.uk"
    prod : "statisticalmethodslibrary.ons.gov.uk"
  }
}