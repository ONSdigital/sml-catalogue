
import os # isort:skip
import boto3 # isort:skip
import logging # isort:skip
import requests # isort:skip

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

def check_website_health(site, expected_string, env):
    """
    check_website_health is a function that calls the site from the event (or environment variables)
    and checks if the status code is 200 and the expected string exists on that site.

    :param site: Url of site to be checked
    :type site: string
    :param expected_string: String of text to be checked
    :type expected_string: String
    :param env: This is for us to distinguish the message between the dev, preprod and prod environments
    :type env: string
    :raises logger.error: will log an error to the lambda log group
    :raises logger.error: variable
    """    

    timeout = 5

    # Ping the site
    response = requests.get(site, timeout=timeout)

    # Define metric data
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

    # If the response code is not 200 or the response text does not 
    # contain the expected string then we log an error and fail the lambda
    if response.status_code != 200:
        print("Metric Data: ", metric_data)
        raise logger.error(f"Error: Status code expected to be 200 but is {response.status_code}")
    
    elif expected_string not in response.text:
        print("Metric Data: ", metric_data)
        raise logger.error(f"Error: Status code is {response.status_code} but expected text \'{expected_string}\' is not found")
    
def lambda_handler(event, context):
    """
    lambda_handler takes variables from the event or environment and calls the healthcheck function

    :param event: Event is the message contents parsed to the lambda
    :type event: string
    :param context: General Lambda term (not used in this case but needed for general setup)
    :type context: N/A
    """    

    print(event)
    
    # To make the lambda reusable we have the option of parsing event data
    # If no event data is provided we default to environment variables
    if 'site' in event:
        site = event['site']
    else:
        site = f"https://{os.environ.get('site')}"

    if 'env' in event:
        env = event['env']
    else:
        env = os.environ.get('env')

    if 'expected_string' in event:
        expected_string = event['expected_string']
    else:
        expected_string = os.environ.get('expected_string')
    
    # Check if website is healthy
    check_website_health(site, expected_string, env)

    