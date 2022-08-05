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

  # backend "local" {
  #   path = "sml-catalogue.tfstate"
  # }

  backend "s3" {
    bucket               = "statistical-methods-library-tf-state"
    key                  = "sml-portal.tfstate"
    region               = "eu-west-2"
    workspace_key_prefix = "workspace"
  }
}
