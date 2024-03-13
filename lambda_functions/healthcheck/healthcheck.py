import logging

import boto3
import requests

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

class HealthCheckException(Exception):
    """
    HealthCheckException Our custom healthcheck exception is to customise our response to the user.

    :param Exception: Exception message to be logged to the healthcheck lambda log group.
    :type Exception: string
    """    
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Custom Exception: {self.message}'

def failing_metric(url, env, expected_string, status_code, failure_type):
    """
    failing_metric This function wll be triggered if our healthcheck fails.
    It will log custom metric data to AWS Cloudwatch Metrics

    :param url: Url of url to be checked
    :type url: string
    :param expected_string: String of text to be checked
    :type expected_string: String
    :param env: This is for us to distinguish the message between the dev, preprod and prod environments
    :type env: string
    :param status_code: The status code value we received from the healthcheck.
    :type status_code: string
    :param failure_type: The failure type helps to distinguish between a response and content failure for metric collection.
    :type failure_type: string
    """    
    # Define metric data
    cloudwatch = boto3.client('cloudwatch')
    metric_data = cloudwatch.put_metric_data(
        MetricData = [
            {
                'MetricName': f'{env}-healthcheck-failures',
                'Dimensions': [
                    {
                    'Name': 'EndpointUrl',
                    'Value': url,
                    },
                    {
                    'Name': 'ExpectedString',
                    'Value': expected_string,
                    },
                    {
                    'Name': 'ResponseStatus',
                    'Value': str(status_code),
                    },
                    {
                    'Name': 'FailureType',
                    'Value': failure_type,
                    },
                ],
                'Unit': 'Count',
                'Value': 1,
            },
        ],
        Namespace = 'SML-Healthcheck.'
    )

    print("Metric Data: ", metric_data)

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
    :param failure_type: The failure type helps to distinguish between a response and content failure for metric collection.
    :type failure_type: string
    :raises HealthCheckException: this custom exception will trigger if the response does not match our expected values.
    :raises HealthCheckException: error
    """
    try:
        response = requests.get(url)  
   
        # If the response code is not 200 or the response text does not 
            # contain the expected string then we log an error and fail the lambda
        if response.status_code != 200:
            failure_type = "UnexpectedResponseCode"
            failing_metric(url, env, expected_string, response.status_code, failure_type)
            raise HealthCheckException(f"Status code expected to be 200 but is {response.status_code}")
        
        elif expected_string not in response.text:
                failure_type = "UnexpectedResponseContent"
                failing_metric(url, env, expected_string, response.status_code, failure_type)
                raise HealthCheckException(f"Status code is {response.status_code} but expected text \'{expected_string}\' is not found") 
    except requests.RequestException as e:  
        raise HealthCheckException(f"Request failed: {e}")
    except Exception as e:  
        raise HealthCheckException(f"Unexpected error: {e}")
    
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
    :raises Exception: will raise a error if there is an issue with the healthcheck.
    :raises Exception: error
    """

    try:  
        check_web_url_health(url=event['url'], env=event['env'], expected_string=event['expected_string'])
    except HealthCheckException as e:  
        error_message = f"Health check failed - {e}"  
        print(error_message) 
        raise Exception(f"Lambda Error: {error_message}")  
    except Exception as e:  
        error_message = f"Unexpected error - {e}"
        print(error_message)
        raise Exception(f"Lambda Error: {error_message}")  

    