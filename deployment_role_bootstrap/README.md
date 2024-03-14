# Roles for the SML Portal

This README is to outline the purpose of the role.tf located within this directory.

The purpose of the role.tf is not for deployment but instead to track what has been manually deployed in the AWS console.

The content of this policy is found in a resource within role.tf called aws_iam_policy.deployment_role_sml_policy. 

Our aim is to eventually improve how roles are generated. However, for now this serves as a back up to the console created IAM policy.