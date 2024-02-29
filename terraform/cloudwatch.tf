# creates the cloudwatch alarm and its dependency on the healthcheck
resource "aws_cloudwatch_metric_alarm" "healthcheck" {
  alarm_name          = "${var.environment}-environment-alarm"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  metric_name         = "Errors"
  namespace           = "AWS/Lambda"
  period              = 300
  statistic           = "Sum"
  threshold           = 3
  alarm_description   = "Alarm for ${var.domain_name_base} has been triggered"
  actions_enabled     = "true"
  alarm_actions       = [aws_sns_topic.sns_topic.arn, aws_lambda_function.alerter.arn]
  treat_missing_data  = "breaching"

  dimensions = {
    FunctionName = aws_lambda_function.healthcheck.function_name
  }

  depends_on          = [aws_lambda_function.healthcheck]
}