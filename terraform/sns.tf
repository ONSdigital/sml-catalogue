# Creates and name the sns topic and assigns target email
resource "aws_sns_topic" "sns_topic" {
  name     = "smlPortalTopic"
}

# Assigns the team email to the sns topic as a subscription
resource "aws_sns_topic_subscription" "email_target" {
  topic_arn = aws_sns_topic.sns_topic.arn

  protocol  = "email"
  endpoint  = "SMLAdmin@ons.gov.uk"
}