
import logging
import requests
import boto3

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

def check_web_url_health(url, expected_string, env):
    """
    check_web_url_health is a function that calls the url from the event
    and checks if the status code is 200 and the expected string exists on that url.

    :param url: Url of url to be checked
    :type url: string
    :param expected_string: String of text to be checked
    :type expected_string: String
    :param env: This is for us to distinguish the message between the dev, preprod and prod environments
    :type env: string
    :raises logger.error: will log an error to the lambda log group
    :raises logger.error: variable
    """

    # Ping the url
    response = requests.get(url)

    # Define metric data
    cloudwatch = boto3.client('cloudwatch')
    metric_data = cloudwatch.put_metric_data(
        MetricData = [
            {
                'MetricName': f'{env}-response',
                'Dimensions': [
                    {
                    'Name': 'EndpointUrl',
                    'Value': '',
                    },
                    {
                    'Name': 'ExpectedString',
                    'Value': '',
                    }
                ],
                'Unit': 'None',
                'Value': 1
            },
        ],
        Namespace = 'SML-Healthcheck.'
    )

    # If the response code is not 200 or the response text does not 
    # contain the expected string then we log an error and fail the lambda
    if response.status_code != 200:
        logger.info(f"Metric Data: , {metric_data}")
        raise logger.error(f"Error: Status code expected to be 200 but is {response.status_code}")
    
    elif expected_string not in response.text:
        logger.info(f"Metric Data: , {metric_data}")
        raise logger.error(f"Error: Status code is {response.status_code} but expected text \'{expected_string}\' is not found")
    
def lambda_handler(event, context):
    """
    lambda_handler takes variables from the event and calls the healthcheck function

    :param event: Event is the message contents passes to the lambda e.g.
                    {
                        "expected_string" = "An open source library for statistical code approved by the ONS",
                        "env" = "dev",
                        "url" = "https://dev-sml.aws.onsdigital.uk/"
                    }
    :type event: string
    :param context: General Lambda term (not used in this case but needed for general setup)
    :type context: N/A
    """    

    print(event)
    
    # To make the lambda reusable we have the option of parsing event data
    # Assign event data
    if 'url' and 'env' and 'expected_string' in event:
        url = event['url']
        env = event['env']
        expected_string = event['expected_string']
        # Check if weburl is healthy
        check_web_url_health(url, expected_string, env)
    else:
        logger.error("The lambda event has missing values, we expect a value for the url, env and expected string")

    