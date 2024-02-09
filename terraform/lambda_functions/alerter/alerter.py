import json # isort:skip
import requests # isort:skip

def lambda_handler(event, context):
    environment = f"https://{os.environ.get('environment')}"
    slack_webhook_url = "https://app.slack.com/client/E04RP3ZJ3QF/C06J7QAQE0Z"
    alert_message = {
        "AlarmName": f"{environment} issue",
        "NewStateValue": "ALARM",
        "NewStateReason": "Threshold Crossed",
    }
    
    response = requests.post(
        slack_webhook_url, 
        data=json.dumps(alert_message),
        headers={'Content-Type': 'application/json'}
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