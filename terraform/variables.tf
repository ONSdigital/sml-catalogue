variable "environment" {
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

variable "s3_bucket" {
  type = object({
    domain_name    = string
    hosted_zone_id = string
  })
}
