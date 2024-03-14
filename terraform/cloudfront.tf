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
      content_security_policy = "script-src 'self' 'sha256-AN/TTkrWvH4W7oCH0w79aph67vAli7rskVQ+0LFPnD4=' 'sha256-FM5wgoZgD+IUY/B3phTcQwLPjMdoyegYYa9Lfsx8a0Q=' 'sha256-FM5wgoZgD+IUY/B3phTcQwLPjMdoyegYYa9Lfsx8a0Q=' 'sha256-QTkwzjnbU+Qv8p+Xz6cexltGK9UI2ShI34bF9k9DpXs=' 'sha256-EMdG31ovSprR0tF3JVid3tnd4Db/rb+0c27xK7EAVts=' 'sha256-Khdmw7GCwPLFjfMGBMpTNcdMf4c+bxQbA3kB831L6KM=' 'sha256-wVoJJ46dUdegqo0mzHo83JJUyjS8RdEfN7I1OlrdMOU=' 'sha256-Lp8Q2eLwjHw/eWeZ5jdkGBt5wP7gIjrZXTt4JuVpYQs=' 'sha256-EMdG31ovSprR0tF3JVid3tnd4Db/rb+0c27xK7EAVts=' https://cdn.ons.gov.uk https://www.googletagmanager.com https://cdnjs.cloudflare.com"
    }
    referrer_policy {
      override        = true
      referrer_policy = "no-referrer"
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