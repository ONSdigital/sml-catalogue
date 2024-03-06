output "aws_cloudwatch_metric_alarm" {
  value = aws_cloudwatch_metric_alarm.healthcheck.arn
}

output "aws_sns_topic" {
  value = aws_sns_topic.sns_topic.arn
}

output "aws_lambda_function" {
  value = aws_lambda_function.healthcheck.arn
}