# Create a route53 and its dependency on the cloudwatch alarm
resource "aws_route53_health_check" "sml" {
  type                            = "CLOUDWATCH_METRIC"
  cloudwatch_alarm_name           = aws_cloudwatch_metric_alarm.healthcheck.alarm_name
  cloudwatch_alarm_region         = "eu-west-2"
  insufficient_data_health_status = "Healthy"

  tags = {
    Name = "${var.environment}_environment"
  }

  depends_on                      = [aws_cloudwatch_metric_alarm.healthcheck]
}