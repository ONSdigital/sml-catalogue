# This rule triggers the healthcheck lambda every minute
resource "aws_cloudwatch_event_rule" "trigger_healthcheck" {
    name                = "${var.domain_name_base}-healthcheck-trigger"
    description         = "Fires the healthcheck lambda function every minute"
    schedule_expression = "rate(1 minute)"
}

# Points to the healthcheck lambda
resource "aws_cloudwatch_event_target" "sml_site_trigger_healthcheck" {
    rule      = "${aws_cloudwatch_event_rule.trigger_healthcheck.name}"
    target_id = "check_sml_site"
    arn       = "${aws_lambda_function.healthcheck.arn}"
    input     = jsonencode({
                  "site"            : "https://${var.domain_name_base}",
                  "env"             : "${var.environment}",
                  "expected_string" : "An open source library for statistical code approved by the ONS"
                })
}

