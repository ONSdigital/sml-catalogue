resource "aws_s3_bucket" "sml-catalogue" {
  bucket        = "sml-portal-${var.environment}-${terraform.workspace}"
  force_destroy = true
}

resource "aws_s3_bucket_ownership_controls" "rule" {
  bucket = aws_s3_bucket.sml-catalogue.id
  rule {
      object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket_acl" "sml-catalogue" {
  depends_on = [aws_s3_bucket_ownership_controls.rule]
  bucket = aws_s3_bucket.sml-catalogue.id
  acl    = "private"
}

data "aws_iam_policy_document" "s3_policy" {
  statement {
    actions   = ["s3:GetObject"]
    resources = ["${aws_s3_bucket.sml-catalogue.arn}/*"]

    principals {
      type        = "AWS"
      identifiers = [aws_cloudfront_origin_access_identity.sml-catalogue.iam_arn]
    }
  }
}

resource "aws_s3_bucket_policy" "sml-catalogue" {
  bucket = aws_s3_bucket.sml-catalogue.id
  policy = data.aws_iam_policy_document.s3_policy.json
}

resource "aws_s3_bucket_public_access_block" "sml-catalogue" {
  bucket = aws_s3_bucket.sml-catalogue.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
