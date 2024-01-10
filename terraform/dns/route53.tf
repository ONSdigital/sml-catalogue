# We're using the domain name base here on its own since
# there's only one host/CF distro per zone, as all dev
# branch deployments are left as CF URLs since they
# do not need to be memorable or static.

data "aws_route53_zone" "sml" {
  name         = var.domain_name_base
  private_zone = false
}

resource "aws_route53_record" "sml" {
  zone_id = data.aws_route53_zone.sml.zone_id
  name    = var.domain_name_base
  type    = "A"
  alias {
    name                   = var.s3_bucket.domain_name
    zone_id                = var.s3_bucket.hosted_zone_id
    evaluate_target_health = false
  }
}

resource "aws_acm_certificate" "sml" {
  domain_name       = var.domain_name_base
  validation_method = "DNS"
  #  provider          = aws.us_east_1
}

resource "aws_acm_certificate_validation" "sml" {
  certificate_arn         = aws_acm_certificate.sml.arn
  validation_record_fqdns = [for record in aws_route53_record.cert-validations : record.fqdn]
  #  provider                = aws.us_east_1
}

resource "aws_route53_record" "cert-validations" {
  for_each = {
    for dvo in aws_acm_certificate.sml.domain_validation_options : dvo.domain_name => {
      name   = dvo.resource_record_name
      record = dvo.resource_record_value
      type   = dvo.resource_record_type
    }
  }
  allow_overwrite = true
  name            = each.value.name
  records         = [each.value.record]
  ttl             = 60
  type            = each.value.type
  zone_id         = data.aws_route53_zone.sml.zone_id
}



resource "aws_route53_health_check" "sml" {
  fqdn              = "dev-sml.aws.onsdigital.uk"
  type              = "HTTPS"
  port              = "443"
  resource_path     = "/"
  failure_threshold = "5"
  request_interval  = "30"
  tags = {
    Name = "sml-health-check"
  }
}

resource "aws_cloudwatch_metric_alarm" "sml_healthcheck_alarm" {
  alarm_name          = "sml-route-53-health_check_alarm"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  metric_name         = "HealthCheckStatus"
  namespace           = "AWS/Route53"
  period              = 60
  statistic           = "Minimum"
  threshold           = 1
  alarm_description   = "This metric monitors sml-route-53-healthchecks"
  actions_enabled     = "true"
  alarm_actions       = [aws_sns_topic.sns_topic.arn]
  treat_missing_data  = "breaching"
  dimensions = {
      HealthCheckId = aws_route53_health_check.sml.id
   }
  depends_on = [
     aws_route53_health_check.sml
    ]
}

resource "aws_sns_topic" "sns_topic" {
    name   = "smlTopic"
}

output "sns_topic_arn" {
 value = aws_sns_topic.sns_topic.arn
}