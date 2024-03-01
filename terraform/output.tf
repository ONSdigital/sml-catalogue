output "cf_website_url" {
  value = "https://${aws_cloudfront_distribution.sml-catalogue.domain_name}/"
}

output "cloudfront_id" {
  value = aws_cloudfront_distribution.sml-catalogue.id
}

output "cert_arn" {
  value = aws_acm_certificate.sml.arn
}

output "website_url" {
  value = "https://${var.domain_name_base}/"
}