locals {
  s3_origin_id = aws_s3_bucket.sml-catalogue.id
}

resource "aws_cloudfront_distribution" "sml-catalogue" {
  origin {
    domain_name = aws_s3_bucket.sml-catalogue.bucket_regional_domain_name
    origin_id   = local.s3_origin_id

    s3_origin_config {
      origin_access_identity = aws_cloudfront_origin_access_identity.sml-catalogue.cloudfront_access_identity_path
    }
  }

  enabled             = true
  is_ipv6_enabled     = true
  default_root_object = "index.html"

  aliases = terraform.workspace == "main" ? [local.domain_name_base[var.environment]] : null

  custom_error_response {
    error_code         = "403"
    response_code      = "404"
    response_page_path = "/page-not-found"
  }
  custom_error_response {
    error_code         = "404"
    response_code      = "404"
    response_page_path = "/page-not-found"
  }

  logging_config {
    include_cookies = false
    bucket          = "statistical-methods-library-cf-logs-${var.environment}.s3.amazonaws.com"
    prefix          = terraform.workspace
  }

  default_cache_behavior {
    allowed_methods  = ["GET", "HEAD"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = local.s3_origin_id

    forwarded_values {
      query_string = false
      headers      = ["Origin"]

      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy     = "redirect-to-https"
    response_headers_policy_id = aws_cloudfront_response_headers_policy.noindex.id

    min_ttl     = 0
    default_ttl = 86400
    max_ttl     = 31536000
  }

  price_class = "PriceClass_100"

  restrictions {
    geo_restriction {
      restriction_type = "whitelist"
      locations        = ["GB"]
    }
  }

  viewer_certificate {
    acm_certificate_arn            = terraform.workspace == "main" ? module.route53[0].cert_arn : null
    ssl_support_method             = terraform.workspace == "main" ? "sni-only" : null
    minimum_protocol_version       = terraform.workspace == "main" ? "TLSv1.2_2021" : null
    cloudfront_default_certificate = terraform.workspace != "main"
  }
}

resource "aws_cloudfront_response_headers_policy" "noindex" {
  name = "noindex-headers-policy-${terraform.workspace}"

  custom_headers_config {
    items {
      header   = "X-Robots-Tag"
      override = true
      value    = "noindex"
    }
    items {
      header   = "Permissions-Policy"
      override = true
      value    = "accelerometer=(),autoplay=(),camera=(),display-capture=(),encrypted-media=(),fullscreen=(),gamepad=(),geolocation=(),gyroscope=(),magnetometer=(),microphone=(),midi=(),payment=(),picture-in-picture=(),publickey-credentials-get=(),sync-xhr=(self),usb=(),screen-wake-lock=(),xr-spatial-tracking=()"
    }
  }
  security_headers_config {
    strict_transport_security {
      override                   = true
      access_control_max_age_sec = 31536000
      include_subdomains         = true
    }
    content_type_options {
      override = true
    }
    xss_protection {
      override   = true
      protection = true
    }
    frame_options {
      override     = true
      frame_option = "DENY"
    }
    content_security_policy {
      override                = true
      content_security_policy = "script-src 'self' 'sha256-AN/TTkrWvH4W7oCH0w79aph67vAli7rskVQ+0LFPnD4=' 'sha256-FM5wgoZgD+IUY/B3phTcQwLPjMdoyegYYa9Lfsx8a0Q=' 'sha256-Khdmw7GCwPLFjfMGBMpTNcdMf4c+bxQbA3kB831L6KM=' 'sha256-wVoJJ46dUdegqo0mzHo83JJUyjS8RdEfN7I1OlrdMOU=' 'sha256-Lp8Q2eLwjHw/eWeZ5jdkGBt5wP7gIjrZXTt4JuVpYQs=' 'sha256-EMdG31ovSprR0tF3JVid3tnd4Db/rb+0c27xK7EAVts=' https://cdn.ons.gov.uk https://www.googletagmanager.com"
    }
    referrer_policy {
      override        = true
      referrer_policy = "no-referrer"
    }
  }
}

resource "aws_cloudfront_origin_access_identity" "sml-catalogue" {
}

resource "aws_cloudwatch_log_group" "healthcheck_lambda_log_group" {
  name              = "/aws/lambda/${var.environment}-healthcheck"
  retention_in_days = 7
}

resource "aws_cloudwatch_event_rule" "trigger_healthcheck" {
    name = "${local.domain_name_base[var.environment]}-healthcheck-trigger"
    description = "Fires the healthcheck lambda function every five minutes"
    schedule_expression = "rate(5 minutes)"
}

resource "aws_cloudwatch_event_target" "sml_site_trigger_healthcheck" {
    rule = "${aws_cloudwatch_event_rule.trigger_healthcheck.name}"
    target_id = "check_sml_site"
    arn = "${aws_lambda_function.healthcheck.arn}"
}

data "aws_iam_policy_document" "lambda_healthcheck" {
  statement {
    actions = [
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents",
    ]

    resources = [
      "arn:aws:logs:*:*:*",
    ]
  }
}

# This creates the policy needed for a lambda to log. #2
resource "aws_iam_policy" "lambda_healthcheck" {
  name   = "lambda-healthcheck-logging"
  path   = "/"
  policy = "${data.aws_iam_policy_document.lambda_healthcheck.json}"
}

# This attaches the policy needed for logging to the lambda's IAM role. #3
resource "aws_iam_role_policy_attachment" "lambda_healthcheck" {
  role       = "${aws_iam_role.lambda_healthcheck.name}"
  policy_arn = "${aws_iam_policy.lambda_healthcheck.arn}"
}

resource "aws_lambda_permission" "allow_cloudwatch_to_call_healthcheck" {
    statement_id = "AllowExecutionFromCloudWatch"
    action = "lambda:InvokeFunction"
    function_name = "${aws_lambda_function.healthcheck.function_name}"
    principal = "events.amazonaws.com"
    source_arn = "${aws_cloudwatch_event_rule.trigger_healthcheck.arn}"
}

data "archive_file" "zip_the_python_lambdas" {
type        = "zip"
source_file  = "./lambda_functions/healthcheck/healthcheck.py"
output_path = "./lambda_functions/healthcheck/healthcheck.zip"
}

data "aws_iam_policy_document" "lambda_role" {
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRole"]

    principals {
      identifiers = ["lambda.amazonaws.com"]
      type        = "Service"
    }
  }
}

resource "aws_iam_role" "lambda_healthcheck" {
  name               = "${local.domain_name_base[var.environment]}-healthcheck"
  assume_role_policy = data.aws_iam_policy_document.lambda_role.json
}

resource "aws_lambda_function" "healthcheck" {
  provider      = aws.eu-west-2
  role          = aws_iam_role.lambda_healthcheck.arn

  function_name = "${var.environment}-healthcheck"

  filename      = "./lambda_functions/healthcheck/healthcheck.zip"

  handler       = "healthcheck.lambda_handler"

  runtime       = "python3.7"
  timeout       = 10
  memory_size   = 512

  environment {
    variables = {
      "site" = local.domain_name_base[var.environment]
    }
  }

  tags = {
    Name = "${var.environment}_sml_lambda_health_check"
  }

  depends_on = [aws_cloudwatch_log_group.healthcheck_lambda_log_group]

}

module "route53" {
  source = "./dns"
  count  = terraform.workspace == "main" ? 1 : 0

  s3_bucket = {
    domain_name    = aws_cloudfront_distribution.sml-catalogue.domain_name
    hosted_zone_id = aws_cloudfront_distribution.sml-catalogue.hosted_zone_id
  }
  domain_name_base = local.domain_name_base[var.environment]
}

resource "aws_route53_health_check" "sml" {
  type                            = "CLOUDWATCH_METRIC"
  cloudwatch_alarm_name           = aws_cloudwatch_metric_alarm.environment_health_check_alarm.alarm_name
  cloudwatch_alarm_region         = "us-east-1"
  insufficient_data_health_status = "Unhealthy"

  depends_on = [aws_cloudwatch_metric_alarm.environment_health_check_alarm]
}

resource "aws_cloudwatch_metric_alarm" "environment_health_check_alarm" {
  provider            = aws.us_east_1
  alarm_name          = "${var.environment}_environment_alarm"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  metric_name         = "health_check_status"
  namespace           = "AWS/Route53"
  period              = 3000
  statistic           = "Minimum"
  threshold           = 3
  alarm_description   = "Alarm for ${var.environment} environment has been triggered"
  actions_enabled     = "true"
  alarm_actions       = [aws_sns_topic.sns_topic.arn]
  treat_missing_data  = "breaching"

  dimensions = {
    FunctionName = aws_lambda_function.healthcheck
  }

  depends_on = [aws_lambda_function.healthcheck]
}

resource "aws_sns_topic" "sns_topic" {
  provider = aws.us_east_1
  name     = "smlPortalTopic"
}

resource "aws_sns_topic_subscription" "email_target" {
  provider = aws.us_east_1
  topic_arn = aws_sns_topic.sns_topic.arn

  protocol  = "email"
  endpoint  = "james.morgan@ons.gov.uk"
}

output "cf_website_url" {
  value = "https://${aws_cloudfront_distribution.sml-catalogue.domain_name}/"
}

output "cloudfront_id" {
  value = aws_cloudfront_distribution.sml-catalogue.id
}

output "website_url" {
  value = length(module.route53) > 0 ? module.route53[0].website_url : "https://${aws_cloudfront_distribution.sml-catalogue.domain_name}/"
}
