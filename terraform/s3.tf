resource "aws_s3_bucket" "sml-catalogue" {
  bucket = "sml-catalogue-${var.suffix}"
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
}
