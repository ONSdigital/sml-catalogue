import requests # isort:skip
import boto3 # isort:skip
import logging # isort:skip

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

def check_website_status(site, expected_string, env):
    timeout = 5

    healthcheck = requests.get(site, timeout=timeout)

    cloudwatch = boto3.client('cloudwatch')
    metric_data = cloudwatch.put_metric_data(
        MetricData = [
            {
                'MetricName': f'{env}-healthcheck',
                'Unit': 'None',
                'Value': 1
            },
        ],
        Namespace = 'AWS/Lamdda'
    )

    if healthcheck.status_code != 200:
        print("Metric Data: ", metric_data)
        raise logger.error(f"Error: Status code expected to be 200 but is {healthcheck.status_code}")
    
    elif expected_string not in healthcheck.text:
        print("Metric Data: ", metric_data)
        raise logger.error(f"Error: Status code is {healthcheck.status_code} but text is expected to be {expected_string} but is not found")
    
def lambda_handler(event, context):

    print(event)
    
    if 'site' in event:
        site = event['site']

    if 'env' in event:
        env = event['env']

    if 'expected_string' in event:
        expected_string = event['expected_string']
    
    check_website_status(site, expected_string, env)

    