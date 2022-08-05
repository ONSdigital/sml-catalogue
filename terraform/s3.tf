resource "aws_s3_bucket" "sml-catalogue" {
  bucket        = "sml-portal-${terraform.workspace}"
  force_destroy = true
}

resource "aws_s3_bucket_acl" "sml-catalogue" {
  bucket = aws_s3_bucket.sml-catalogue.id
  acl    = "private"
}

resource "aws_s3_bucket_website_configuration" "sml-catalogue" {
  bucket = aws_s3_bucket.sml-catalogue.bucket

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "page-not-found"
  }
}

output "website_url" {
  value = "http://${aws_s3_bucket_website_configuration.sml-catalogue.website_endpoint}/"
}
