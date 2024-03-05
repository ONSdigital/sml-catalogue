# Adds permission for cloudwatch to invoke alerter function
resource "aws_lambda_permission" "allow_cloudwatch_to_invoke_alerter" {
    statement_id  = "AlarmAction"
    action        = "lambda:InvokeFunction"
    function_name = "${aws_lambda_function.alerter.function_name}"
    principal     = "lambda.alarms.cloudwatch.amazonaws.com"
    source_arn    = "${aws_cloudwatch_metric_alarm.healthcheck.arn}"
}

# Creates iam role
resource "aws_iam_role" "alerter" {
  name               = "${var.environment}-alerter"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

# Creates alerter lambda
resource "aws_lambda_function" "alerter" {
  role          = aws_iam_role.alerter.arn

  function_name = "${var.environment}-alerter"

  filename      = "../../lambda_functions.zip/alerter.py"

  handler       = "alerter.lambda_handler"

  runtime       = "python3.9"
  timeout       = 10
  memory_size   = 512

  tags = {
    Name = "${var.environment}_sml_lambda_alerter"
  }

}