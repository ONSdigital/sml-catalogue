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
    cloudfront_default_certificate = true
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

output "cf_website_url" {
  value = "https://${aws_cloudfront_distribution.sml-catalogue.domain_name}/"
}

output "cloudfront_id" {
  value = aws_cloudfront_distribution.sml-catalogue.id
}
