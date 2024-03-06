variable "environment" {
  type = string
}

locals {
  domain_name_base = {
    dev : "dev-sml.aws.onsdigital.uk"
    preprod : "preprod-sml.aws.onsdigital.uk"
    prod : "statisticalmethodslibrary.ons.gov.uk"
  }
}

variable "expected_string" {
  type = string
  default = "An open source library for statistical code approved by the ONS"
}

variable "email" {
  type = string
  default = "SMLAdmin@ons.gov.uk"
}

variable "alerter" {
  type = string
}