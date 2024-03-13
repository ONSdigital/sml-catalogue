# Adds permission for cloudwatch to invoke alerter function
resource "aws_lambda_permission" "allow_cloudwatch_to_invoke_alerter" {
    statement_id  = "AlarmAction"
    action        = "lambda:InvokeFunction"
    function_name = "${var.environment}-alerter-{terraform.workspace}"
    principal     = "lambda.alarms.cloudwatch.amazonaws.com"
    source_arn    = "${aws_cloudwatch_metric_alarm.healthcheck.arn}"
}

# Creates the cloudwatch alarm and its dependency on the healthcheck
resource "aws_cloudwatch_metric_alarm" "healthcheck" {
  alarm_name          = "${var.environment}-environment-healthcheck-alarm"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  metric_name         = "Errors"
  namespace           = "AWS/Lambda"
  period              = 300
  statistic           = "Sum"
  threshold           = 3
  alarm_description   = "Alarm for ${local.domain_name_base[var.environment]} has been triggered"
  actions_enabled     = "true"
  alarm_actions       = [aws_sns_topic.sns_topic.arn, var.alerter]
  treat_missing_data  = "breaching"

  dimensions = {
    FunctionName = aws_lambda_function.healthcheck.function_name
  }

  depends_on          = [aws_lambda_function.healthcheck]
}