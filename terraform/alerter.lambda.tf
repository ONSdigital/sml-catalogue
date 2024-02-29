# Adds permission for cloudwatch to invoke alerter function
resource "aws_lambda_permission" "allow_cloudwatch_to_invoke_alerter" {
    statement_id  = "AlarmAction"
    action        = "lambda:InvokeFunction"
    function_name = "${aws_lambda_function.alerter.function_name}"
    principal     = "lambda.alarms.cloudwatch.amazonaws.com"
    source_arn    = "${aws_cloudwatch_metric_alarm.healthcheck.arn}"
}

# zip alerter lambda for deployment to aws
data "archive_file" "zip_the_python_alerter_lambda" {
type        = "zip"
source_file = "./healthcheck/lambda_functions/alerter/alerter.py"
output_path = "./healthcheck/lambda_functions/alerter/alerter.zip"
}

# creates iam role
resource "aws_iam_role" "alerter" {
  name               = "${var.environment}-alerter"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

# creates alerter lambda
resource "aws_lambda_function" "alerter" {
  role          = aws_iam_role.alerter.arn

  function_name = "${var.environment}-alerter"

  filename      = "./healthcheck/lambda_functions/alerter/alerter.zip"

  handler       = "alerter.lambda_handler"

  runtime       = "python3.9"
  timeout       = 10
  memory_size   = 512

  environment {
    variables = {
      "alarm_name" = "${var.environment}-environment-alarm",
      "lambda_name" = "${var.environment}-healthcheck",
      "url" = local.domain_name_base[var.environment],
      "slack_webhook_url" = "https://hooks.slack.com/triggers/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"
    }
  }

  tags = {
    Name = "${var.environment}_sml_lambda_alerter"
  }

}