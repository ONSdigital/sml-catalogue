import os # isort:skip
import requests # isort:skip
import boto3 # isort:skip

def check_website_status(site, expected_string):
    timeout = 5

    print("Url: ", site, "Expected text: ", expected_string)

    response = requests.get(site, timeout=timeout)

    if response.status_code != 200:
        raise ValueError(f"Error: Status code is {response.status_code}")
    
    elif expected_string not in response.text:
        raise ValueError(f"Error: Status code is {response.status_code} but text does not match expected string")
    else:
        return {
        'statusCode': 200,
        'body': 'Success'
        }
        
def lambda_handler(event, context):
    
    if 'site' in event:
        site = event['site']

    if 'env' in event:
        env = event['env']

    if 'expected_string' in event:
        expected_string = event['expected_string']
        
    check_website_status(site, expected_string)

    cloudwatch = boto3.client('cloudwatch')
    response = cloudwatch.put_metric_data(
        MetricData = [
            {
                'MetricName': f'{env}-healthcheck',
                'Unit': 'None',
                'Value': 1
            },
        ],
        Namespace = 'AWS/Lamdda'
    )

    return response