variable "lambda_name_suffix" {
  type = string
}

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

locals {
  schema_domain_name_base = {
    dev : "https://dev-sml.aws.onsdigital.uk"
    preprod : "https://preprod-sml.aws.onsdigital.uk"
    prod : "https://statisticalmethodslibrary.ons.gov.uk"
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