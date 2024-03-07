import json
import logging
import os

import requests

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

def lambda_handler(event, context):
    """
    lambda_handler The purpose of this lambda function is to alert the sml-portal-alert
    slack channel if an alarm is failing (failing alarm triggers lambda)

    :param event: Event is the message contents parsed to the lambda e.g.
                  {
                  "alarm_name" = "${var.environment}-environment-alarm",
                  "lambda_name" = "${var.environment}-healthcheck",
                  "url" = var.domain_name_base[var.environment],
                  "slack_webhook_url" = aws secret
                  }
    :type event: string
    :param context: General Lambda term (not used in this case but needed for general setup)
    :type context: N/A
    :return: Return a success or failure outcome on whether the slack message was sent
    :rtype: json
    """ 
    print(event)
    
    # To make the lambda reusable we have the option of parsing event data
    # If no event data is provided we default to environment variables
    if 'lambda_name' in event:
        lambda_name = event['lambda_name']
    else:
        logger.info("Lambda name is missing")
        lambda_name = os.environ.get("lambda_name")

    if 'alarm_name' in event:
        alarm_name = event['alarm_name']
    else:
        logger.info("Alarm name is missing")
        alarm_name = os.environ.get("alarm_name")

    if 'url' in event:
        url = event['url']
    else:
        logger.info("Url is missing")
        url = os.environ.get("url")

    if 'slack_webhook_url' in event:
        slack_webhook_url = event['slack_webhook_url']
    else:
        logger.info("Slack webhook url is missing")
        slack_url_prefix = os.environ.get("slack_url")
        slack_webhook_secret = os.getenv("slack_secret")
        slack_webhook_url = f"{slack_url_prefix}/{slack_webhook_secret}"

    print('slack_secret', slack_webhook_url)

    # Message sent to channel
    alert_message = {
        "Summary": f"The website at {url} is unreachable. Healthcheck failure.",
        "Alarm": "Route53 Health Check Failure",
        "Description": f"Website is unreachable or not returning the expected response. Check Amazon Cloudwatch Alarms \'{alarm_name}\' and Healthcheck Lambda \'{lambda_name}\'.",
    }

    try:
        # Send the request
        requests.get(
            slack_webhook_url,
            timeout=5,
            data=json.dumps(alert_message).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Message sent to Slack successfully')
        }
    except Exception as e:
        logger.error("Error sending message to Slack:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps('Error sending message to Slack')
        }