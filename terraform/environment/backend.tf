
terraform {
  backend "s3" {
    region   = "eu-west-2"
    role_arn = "arn:aws:iam::289259348294:role/spp-concourse-access-prod"
  }
}