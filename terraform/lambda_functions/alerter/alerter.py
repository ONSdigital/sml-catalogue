import os # isort:skip
import json # isort:skip
import requests # isort:skip

def lambda_handler(event, context):
    
    if 'environment' in event:
        environment = event['environment']
    else:
        environment = f"https://{os.environ.get('environment')}"

    if 'slack_webhook_url' in event:
        slack_webhook_url = event['slack_webhook_url']
    else:
        slack_webhook_url = f"{os.environ.get('slack_webhook_url')}"


    timeout=5
    alert_message = {
        "AlarmName": f"{environment} \'s alarm has converted from an \'OK\' state to \'In alarm\' state",
        "NewStateValue": "ALARM",
        "NewStateReason": "Error has occurred because the site cannot be reached or content does not match expected values. Go to the healthcheck lambda log group for more information",
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