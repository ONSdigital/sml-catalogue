# This rule triggers the healthcheck lambda every minute
resource "aws_cloudwatch_event_rule" "trigger_healthcheck" {
    name                = "${var.domain_name_base[var.environment]}-healthcheck-trigger"
    description         = "Fires the healthcheck lambda function every minute"
    schedule_expression = "rate(1 minute)"
}

# Targets the healthcheck lambda
resource "aws_cloudwatch_event_target" "sml_site_trigger_healthcheck" {
    rule      = "${aws_cloudwatch_event_rule.trigger_healthcheck.name}"
    target_id = "check_sml_site"
    arn       = "${aws_lambda_function.healthcheck.arn}"
    input     = jsonencode({
                  "url"            : "${var.input.url}",
                  "env"             : "${var.environment}",
                  "expected_string" : "${var.input.text}"
                })
}

# Adds permission for event to invoke healthcheck function
resource "aws_lambda_permission" "allow_event_to_invoke_healthcheck" {
    statement_id  = "AlarmAction"
    action        = "lambda:InvokeFunction"
    function_name = "${aws_lambda_function.healthcheck.function_name}"
    principal     = "events.amazonaws.com"
    source_arn    = "${aws_cloudwatch_event_rule.trigger_healthcheck.arn}"
}