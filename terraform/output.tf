output "cf_website_url" {
  value = "https://${aws_cloudfront_distribution.sml-catalogue.domain_name}/"
}

output "cloudfront_id" {
  value = aws_cloudfront_distribution.sml-catalogue.id
}

output "cert_arn" {
  source = "./dns"
  value = aws_acm_certificate.sml.arn
}

output "website_url" {
  value = length(module.route53) > 0 ? module.route53[0].website_url : "https://${aws_cloudfront_distribution.sml-catalogue.domain_name}/"
}