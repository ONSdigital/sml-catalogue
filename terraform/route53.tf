data "aws_route53_zone" "onsdigital" {
  name         = local.domain_name_base[var.account]
  private_zone = false
}

resource "aws_route53_record" "onsdigital" {
  zone_id = data.aws_route53_zone.onsdigital.zone_id
  name    = aws_s3_bucket.sml-catalogue.id
  type    = "A"
  alias {
    name                   = aws_cloudfront_distribution.sml-catalogue.domain_name
    zone_id                = aws_cloudfront_distribution.sml-catalogue.hosted_zone_id
    evaluate_target_health = false
  }
}

resource "aws_acm_certificate" "sml" {
  domain_name       = aws_s3_bucket.sml-catalogue.id
  validation_method = "DNS"
  provider          = aws.us_east_1
}

resource "aws_acm_certificate_validation" "sml" {
  certificate_arn         = aws_acm_certificate.sml.arn
  validation_record_fqdns = [for record in aws_route53_record.cert-validations : record.fqdn]
  provider                = aws.us_east_1
}
resource "aws_route53_record" "cert-validations" {
  count = length(aws_acm_certificate.sml.domain_validation_options)

  zone_id = data.aws_route53_zone.onsdigital.zone_id
  name    = element(aws_acm_certificate.sml.domain_validation_options.*.resource_record_name, count.index)
  type    = element(aws_acm_certificate.sml.domain_validation_options.*.resource_record_type, count.index)
  records = [element(aws_acm_certificate.sml.domain_validation_options.*.resource_record_value, count.index)]
  ttl     = 60
}

output "website_url" {
  value = "https://${aws_s3_bucket.sml-catalogue.id}/"
}
