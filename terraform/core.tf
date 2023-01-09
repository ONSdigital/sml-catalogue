provider "aws" {
  region = "eu-west-2"

  default_tags {
    tags = {
      ManagedBy                 = "Terraform"
      Name                      = "SML Catalogue"
      "ons:owner:business-unit" = "DST"
      "ons:application:eol"     = "N/A"
      "ons:owner:contact"       = "Steve Gibbard"
      "ons:owner:team"          = "SPP SML"
      "ons:application:name"    = "SML Catalogue"
      "ons:deployment"          = terraform.workspace


    }
  }
}

provider "aws" {
  region = "us-east-1"
  alias  = "us_east_1"

  default_tags {
    tags = {
      ManagedBy                 = "Terraform"
      Name                      = "SML Catalogue"
      "ons:owner:business-unit" = "DST"
      "ons:application:eol"     = "N/A"
      "ons:owner:contact"       = "Steve Gibbard"
      "ons:owner:team"          = "SPP SML"
      "ons:application:name"    = "SML Catalogue"
      "ons:deployment"          = terraform.workspace


    }
  }
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }

  backend "s3" {
    region = "eu-west-2"
  }
}
