output "cert_arn" {
  value = aws_acm_certificate.sml.arn
}

output "website_url" {
  value = "https://${var.domain_name_base}/"
}