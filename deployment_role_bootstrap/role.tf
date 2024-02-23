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
          "token.actions.githubusercontent.com:sub" = "repo:ONSdigital/sml-catalogue:environment:${var.environment}"
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
                "Resource": "arn:aws:s3:::statistical-methods-library-tf-state*"
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
                    "arn:aws:s3:::statistical-methods-library-cf-logs*"
                ]
            },
            {
            "Sid": "AllowRoute53PlusACM",
            "Effect": "Allow",
            "Action": [
                "route53:GetChange",
                "route53:GetHostedZone",
                "route53:ListHostedZones",
                "route53:ChangeResourceRecordSets",
                "route53:CreateHealthCheck",
                "route53:DeleteHealthCheck",
                "route53:UpdateHealthCheck",
                "route53:ChangeTagsForResource",
                "route53:GetHealthCheck",
                "route53:ListTagsForResources",
                "route53:ListTagsForResource",
                "route53:ListResourceRecordSets",
                "sns:CreateTopic",
                "sns:ListTopics",
                "sns:SetTopicAttributes",
                "sns:GetTopicAttributes",
                "sns:DeleteTopic",
                "sns:Publish",
                "sns:ListTagsForResource",
                "sns:TagResource",
                "sns:Subscribe",
                "sns:Unsubscribe",
                "sns:GetSubscriptionAttributes",
                "lambda:CreateFunction",
                "lambda:GetFunction",
                "lambda:TagResource",
                "lambda:UpdateFunctionCode",
                "lambda:RemovePermission",
                "lambda:DeleteFunction",
                "lambda:GetPolicy",
                "lambda:PublishLayerVersion",
                "lambda:ListLayers",
                "lambda:DeleteLayerVersion",
                "lambda:AddLayerVersionPermission",
                "lambda:RemoveLayerVersionPermission",
                "lambda:GetLayerVersion",
                "lambda:InvokeFunction",
                "lambda:ListVersionsByFunction",
                "lambda:GetFunctionCodeSigningConfig",
                "lambda:UpdateFunctionConfiguration",
                "lambda:AddPermission",
                "iam:PassRole",
                "iam:CreateRole",
                "iam:DeleteRole",
                "iam:GetRole",
                "iam:DetachRolePolicy",
                "iam:UpdateAssumeRolePolicy",
                "iam:ListRolePolicies",
                "iam:ListInstanceProfilesForRole",
                "iam:CreatePolicyVersion",
                "iam:DeletePolicyVersion",
                "iam:ListAttachedRolePolicies",
                "iam:CreatePolicy",
                "iam:GetPolicy",
                "iam:ListPolicyTags",
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetRolePolicy",
                "iam:DeletePolicy",
                "iam:ListPolicyVersions",
                "iam:AttachRolePolicy",
                "cloudwatch:DeleteAlarms",
                "cloudwatch:DescribeAlarms",
                "cloudwatch:PutMetricData",
                "cloudwatch:PutMetricAlarm",
                "cloudwatch:ListTagsForResource",
                "acm:AddTagsToCertificate",
                "acm:RenewCertificate",
                "acm:ListTagsForCertificate",
                "acm:DescribeCertificate",
                "acm:DeleteCertificate",
                "acm:RequestCertificate",
                "acm:RemoveTagsFromCertificate",
                "acm:ListCertificates",
                "cloudfront:*",
                "events:PutRule",
                "events:DescribeRule",
                "events:DeleteRule",
                "events:ListRules",
                "events:ListRuleNamesByTarget",
                "events:ListTagsForResource",
                "events:PutTargets",
                "events:ListTargetsByRule",
                "events:RemoveTargets",
                "logs:PutLogEvents",
                "logs:DescribeLogStreams",
                "logs:CreateLogStream",
                "logs:CreateLogGroup",
                "logs:DeleteLogGroup",
                "logs:DescribeLogGroups",
                "logs:ListTagsLogGroup",
                "logs:DeleteRetentionPolicy",
                "logs:PutRetentionPolicy"
            ],
            "Resource": "*"
        }
        ]
    }
    EOF
}


resource "aws_iam_role_policy_attachment" "deployment_role_sml_attachement" {
  role       = aws_iam_role.deployment_role_sml.name
  policy_arn = aws_iam_policy.deployment_role_sml_policy.arn
}
