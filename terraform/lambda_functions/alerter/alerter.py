import os # isort:skip
import json # isort:skip
import requests # isort:skip

def lambda_handler(event, context):
    timeout=5
    environment = f"https://{os.environ.get('environment')}"
    slack_webhook_url = "https://hooks.slack.com/triggers/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"
    alert_message = {
        "AlarmName": f"{environment} issue",
        "NewStateValue": "ALARM",
        "NewStateReason": "Threshold Crossed",
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