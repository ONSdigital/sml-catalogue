# Run via ci-bootstrap/bin/deploy.sh

//---------------------------------------------------------
// Setup

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
      "ons:deployment"          = "account"


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


//---------------------------------------------------------
// Access via Identity Account
resource "aws_iam_role" "deployment_role_sml" {
  name        = "sml-deployment-role"
  description = "Deployment role for the SML portal"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = {
      Effect = "Allow"
      Action = [
        "sts:AssumeRoleWithWebIdentity"
      ]
      Principal = {
        Federated = aws_iam_openid_connect_provider.github.arn
      }
      Condition = {
        StringLike = {
          "token.actions.githubusercontent.com:aud" = "sts.amazonaws.com",
          "token.actions.githubusercontent.com:sub" = "repo:ONSdigital/sml-catalogue:*"
        }
      }
    }
  })
}


resource "aws_iam_openid_connect_provider" "github" {
  url = "https://token.actions.githubusercontent.com"

  client_id_list = [
    "sts.amazonaws.com"
  ]

  thumbprint_list = ["6938fd4d98bab03faadb97b34396831e3780aea1"]
}

resource "aws_iam_policy" "deployment_role_sml_policy" {
  name   = "DeploymentRoleSMLPolicy"
  policy = <<-EOF
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AllowCloudfrontSetup",
                "Effect": "Allow",
                "Action": "cloudfront:*",
                "Resource": "*"
            },
            {
                "Sid": "AllowTFFileAccess",
                "Effect": "Allow",
                "Action": [
                    "s3:PutObject",
                    "s3:GetObject",
                    "s3:DeleteObject"
                ],
                "Resource": "arn:aws:s3:::statistical-methods-library-tf-state*/*"
            },
            {
                "Sid": "AllowTerraformStateBucketAccess",
                "Effect": "Allow",
                "Action": [
                    "s3:ListBucket"
                ],
                "Resource": "arn:aws:s3:::statistical-methods-library-tf-state"
            },
            {
                "Sid": "AllowDeploymentBucketAccess",
                "Effect": "Allow",
                "Action": "s3:*",
                "Resource": [
                    "arn:aws:s3:::sml-portal-*",
                    "arn:aws:s3:::sml-portal-*/*"
                ]
            },
            {
                "Sid": "AllowLogBucketAccess",
                "Effect": "Allow",
                "Action": [
                    "s3:GetBucketAcl",
                    "s3:PutBucketAcl"
                ],
                "Resource": [
                    "arn:aws:s3:::statistical-methods-library-cf-logs"
                ]
            }
        ]
    }
    EOF
}


resource "aws_iam_role_policy_attachment" "deployment_role_sml_attachement" {
  role       = aws_iam_role.deployment_role_sml.name
  policy_arn = aws_iam_policy.deployment_role_sml_policy.arn
}
