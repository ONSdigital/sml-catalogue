# This rule triggers the healthcheck lambda every minute
resource "aws_cloudwatch_event_rule" "trigger_healthcheck" {
    name                = "${local.domain_name_base[var.environment]}-healthcheck-trigger"
    description         = "Fires the healthcheck lambda function every minute"
    schedule_expression = "rate(1 minute)"
    policy - aws_iam_policy_document.event.arn
}

# Points to the healthcheck lambda
resource "aws_cloudwatch_event_target" "sml_site_trigger_healthcheck" {
    rule      = "${aws_cloudwatch_event_rule.trigger_healthcheck.name}"
    target_id = "check_sml_site"
    arn       = "${aws_lambda_function.healthcheck.arn}"
    input     = jsonencode({
                  "site"            : "https://${local.domain_name_base[var.environment]}",
                  "env"             : "${var.environment}",
                  "expected_string" : "An open source library for statistical code approved by the ONS"
                })
}

# Adds permission for event to invoke healthcheck function
data "aws_iam_policy_document" "event" {statement
    effect = "Allow"

    principals {
      type        = "*"
      identifiers = ["*"]
    }

    actions = [
                "events:PutRule",
                "events:DescribeRule",
                "events:DeleteRule",
                "events:ListRules",
                "events:ListRuleNamesByTarget",
                "events:ListTagsForResource",
                "events:PutTargets",
                "events:ListTargetsByRule",
                "events:RemoveTargets"
              ],

    resources = [
      "arn:aws:events:eu-west-2:115311790871:rule/${local.domain_name_base[var.environment]}-healthcheck-trigger",
    ]
}

# Adds permission for event to invoke healthcheck function
resource "aws_lambda_permission" "allow_event_to_invoke_healthcheck" {
    statement_id  = "AlarmAction"
    action        = "lambda:InvokeFunction"
    function_name = "${aws_lambda_function.healthcheck.function_name}"
    principal     = "events.amazonaws.com"
    source_arn    = "${aws_cloudwatch_event_rule.trigger_healthcheck.arn}"
}