import logging

import boto3
import requests

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

def check_web_url_health(url, env, expected_string):
    """
    check_web_url_health is a function that calls the url from the event
    and checks if the status code is 200 and the expected string exists on that url.

    :param url: Url of url to be checked
    :type url: string
    :param expected_string: String of text to be checked
    :type expected_string: String
    :param env: This is for us to distinguish the message between the dev, preprod and prod environments
    :type env: string
    :raises RuntimeError: will raise a error if the response is not received.
    :raises RuntimeError: error
    :raises ValueError: will raise a error if the status code returned by the healthcheck ping is not 200 or the text does not match the expected string.
    :raises ValueError: error
    """
    response = requests.get(url, timeout=5)

    # Define metric data
    cloudwatch = boto3.client('cloudwatch')
    metric_data = cloudwatch.put_metric_data(
        MetricData = [
            {
                'MetricName': f'{env}-response',
                'Dimensions': [
                    {
                    'Name': 'EndpointUrl',
                    'Value': url,
                    },
                    {
                    'Name': 'ExpectedString',
                    'Value': expected_string,
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
        print(f"Metric Data: , {metric_data}")
        raise logger.error(f"Error: Status code expected to be 200 but is {response.status_code}")

    elif expected_string not in response.text:
        print(f"Metric Data: , {metric_data}")
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

    print("Event: ", event)

    if 'url' and 'env' and 'expected_string' in event:
        check_web_url_health(url=event['url'], env=event['env'], expected_string=event['expected_string'])
    else:
        raise logger.error("The lambda event has missing values, we expect a value for the url, env and expected string")

    