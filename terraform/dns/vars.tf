var "s3_bucket" {
  type = object({
    domain_name    = string
    hosted_zone_id = string
  })
}

var "domain_name_base" {
  type = string
}

output "cert_arn" {
  value = aws_acm_certificate.arn
}
