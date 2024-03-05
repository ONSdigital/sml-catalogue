import json
import os
import requests

def lambda_handler(event, context):
    """
    lambda_handler The purpose of this lambda function is to alert the sml-portal-alert
    slack channel if an alarm is failing (failing alarm triggers lambda)

    :param event: Event is the message contents parsed to the lambda e.g.
                  {
                  "alarm_name" = "${var.environment}-environment-alarm",
                  "lambda_name" = "${var.environment}-healthcheck",
                  "url" = var.domain_name_base[var.environment],
                  "slack_webhook_url" = ""
                  }
    :type event: string
    :param context: General Lambda term (not used in this case but needed for general setup)
    :type context: N/A
    :return: Return a success or failure outcome on whether the slack message was sent
    :rtype: json
    """    
    
    # To make the lambda reusable we have the option of parsing event data
    # If no event data is provided we default to environment variables
    if 'lambda_name' in event:
        lambda_name = event['lambda_name']
    
    if 'alarm_name' in event:
        alarm_name = event['alarm_name']
    
    if 'url' in event:
        url = event['url']

    # Slack channel link for alerting purposes
    if 'slack_webhook_url' in event:
        slack_webhook_url = event['slack_webhook_url']

    # Message sent to channel
    alert_message = {
        "Summary": f"The website at {url} is unreachable. Healthcheck failure.",
        "Alarm": "Route53 Health Check Failure",
        "Description": f"Website is unreachable or not returning the expected response. Check Amazon Cloudwatch Alarms \'{alarm_name}\' and Healthcheck Lambda \'{lambda_name}\'.",
    }

    try:
        # Send the request
        response = requests.get(
            slack_webhook_url,
            data=json.dumps(alert_message).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )

        print("Message sent to Slack successfully:", response.text)
        return {
            'statusCode': 200,
            'body': json.dumps('Message sent to Slack successfully')
        }
    except Exception as e:
        print("Error sending message to Slack:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps('Error sending message to Slack')
        }