import os # isort:skip
import requests # isort:skip

def alerter(site):
    alarm_message = {
        "AlarmName": "",
        "Site": f"{site}",
        "NewStateValue": "ALARM",
        "NewStateReason": "Threshold Crossed",
    }

    print(alarm_message)
        
def lambda_handler(event, context):
    
    site = f"https://{os.environ.get('site')}"
    
    result = alerter(site)

    return result