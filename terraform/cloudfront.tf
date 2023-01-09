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
    minimum_protocol_version       = terraform.workspace == "main" ? "TLSv1.2_2019" : null
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
  }
}

resource "aws_cloudfront_origin_access_identity" "sml-catalogue" {
}

module "route53" {
  source = "./dns"
  count  = terraform.workspace == "main" ? 1 : 0
  providers = {
    aws = aws.us_east_1
  }

  s3_bucket = {
    domain_name    = aws_cloudfront_distribution.sml-catalogue.domain_name
    hosted_zone_id = aws_cloudfront_distribution.sml-catalogue.hosted_zone_id
  }
  domain_name_base = local.domain_name_base[var.environment]
}

output "cf_website_url" {
  value = length(module.route53) > 0 ? "https://${aws_cloudfront_distribution.sml-catalogue.domain_name}/" : null
}

output "cloudfront_id" {
  value = length(module.route53) > 0 ? aws_cloudfront_distribution.sml-catalogue.id : null
}

output "website_url" {
 value = length(module.route53) > 0 ? module.route53[0].website_url : null
}
