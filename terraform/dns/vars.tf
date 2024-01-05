variable "s3_bucket" {
  type = object({
    domain_name    = string
    hosted_zone_id = string
  })
}

variable "domain_name_base" {
  type = string
}

output "cert_arn" {
  value = aws_acm_certificate.sml.arn
}

output "website_url" {
  value = "https://${var.domain_name_base}/"
}

variable "region" {
  type    = string
  default = "eu-west-1"
}