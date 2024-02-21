
import requests # isort:skip
import os # isort:skip
import boto3 # isort:skip
import logging # isort:skip

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

def check_website_status(site, expected_string, env):
    timeout = 5

    response = requests.get(site, timeout=timeout)

    cloudwatch = boto3.client('cloudwatch')
    metric_data = cloudwatch.put_metric_data(
        MetricData = [
            {
                'MetricName': f'{env}-response',
                'Unit': 'None',
                'Value': 1
            },
        ],
        Namespace = 'AWS/Lambda'
    )

    if response.status_code != 200:
        print("Metric Data: ", metric_data)
        raise logger.error(f"Error: Status code expected to be 200 but is {response.status_code}")
    
    elif expected_string not in response.text:
        print("Metric Data: ", metric_data)
        raise logger.error(f"Error: Status code is {response.status_code} but expected text \'{expected_string}\' is not found")
    
def lambda_handler(event, context):

    print(event)
    
    if 'site' in event:
        site = event['site']
    else:
        site = os.environ.get('site')

    if 'env' in event:
        env = event['env']
    else:
        env = os.environ.get('env')

    if 'expected_string' in event:
        expected_string = event['expected_string']
    else:
        expected_string = os.environ.get('expected_string')
    
    check_website_status(site, expected_string, env)

    