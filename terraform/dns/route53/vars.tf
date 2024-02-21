output "cert_arn" {
  value = aws_acm_certificate.sml.arn
}

output "website_url" {
  value = "https://${local.domain_name_base}/"
}

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
