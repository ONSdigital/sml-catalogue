provider "aws" {
  region = "eu-west-2"

  default_tags {
    tags = {
      ManagedBy                 = "Terraform"
      Name                      = "SML Catalogue"
      "ons:owner:business-unit" = "DST"
      "ons:application:eol"     = "N/A"
      "ons:owner:contact"       = "Phil Bambridge"
      "ons:owner:team"          = "SPP CMT"
      "ons:application:name"    = "SML Catalogue"
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

  backend "local" {
    path = "sml-catalogue.tfstate"
  }

  #   backend "s3" {
  #     bucket = "sml-catalogue-state"
  #     key    = "sml-catalogue.tfstate"
  #     region = "eu-west-2"
  #   }
}
