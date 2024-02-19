import os # isort:skip
import json # isort:skip
import requests # isort:skip

def lambda_handler(event, context):
    
    if 'lambda_name' in event:
        lambda_name = event['lambda_name']
    else:
        lambda_name = f"https://{os.environ.get('lambda_name')}"
    
    if 'alarm_name' in event:
        alarm_name = event['alarm_name']
    else:
        alarm_name = f"https://{os.environ.get('alarm_name')}"
    
    if 'url' in event:
        url = event['url']
    else:
        url = f"https://{os.environ.get('url')}"

    if 'slack_webhook_url' in event:
        slack_webhook_url = event['slack_webhook_url']
    else:
        slack_webhook_url = f"{os.environ.get('slack_webhook_url')}"


    timeout=5
    alert_message = {
        "Summary": f"The website at {url} is unreachable. Healthcheck failure",
        "Alarm": "Route53 Health Check Failure",
        "Description": f"Website is unreachable or not returning the expected response. Check Amazon Cloudwatch Alarms {alarm_name} and Healthcheck Lambda {lambda_name}",
    }
    
    response = requests.post(
        slack_webhook_url, 
        data=json.dumps(alert_message),
        headers={'Content-Type': 'application/json'},
        timeout=timeout
    )
    
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