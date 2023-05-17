
terraform {
  backend "s3" {
    region   = "eu-west-2"
    role_arn = "arn:aws:iam::115311790871:role/spp-concourse-sml-deployment-dev"
  }
}