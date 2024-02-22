import os # isort:skip
import json # isort:skip
import requests # isort:skip

def alerter(event, context):
    """
    alerter The purpose of this lambda function is to alert the sml-portal-alert
    slack channel if an alarm is failing (failing alarm triggers lambda)

    :param event: Event is the message contents parsed to the lambda
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
    else:
        lambda_name = os.environ.get('lambda_name')
    
    if 'alarm_name' in event:
        alarm_name = event['alarm_name']
    else:
        alarm_name = os.environ.get('alarm_name')
    
    if 'url' in event:
        url = event['url']
    else:
        url = f"https://{os.environ.get('url')}"

    # Slack channel link for alerting purposes
    if 'slack_webhook_url' in event:
        slack_webhook_url = event['slack_webhook_url']
    else:
        slack_webhook_url = f"{os.environ.get('slack_webhook_url')}"

    timeout=5

    # Message sent to channel
    alert_message = {
        "Summary": f"The website at {url} is unreachable. Healthcheck failure.",
        "Alarm": "Route53 Health Check Failure",
        "Description": f"Website is unreachable or not returning the expected response. Check Amazon Cloudwatch Alarms \'{alarm_name}\' and Healthcheck Lambda \'{lambda_name}\'.",
    }
    
    # We post the message to the slack channel workflow
    response = requests.post(
        slack_webhook_url, 
        data=json.dumps(alert_message),
        headers={'Content-Type': 'application/json'},
        timeout=timeout
    )
    
    # Check if post was successful
    if response.status_code == 200:
        return {
            'statusCode': 200,
            'body': json.dumps('Message sent successfully')
        }
    else:
        return {
            'statusCode': response.status_code,
            'body': json.dumps('Failed to send message')
        }