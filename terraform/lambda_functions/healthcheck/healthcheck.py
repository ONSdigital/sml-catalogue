import os # isort:skip
import requests # isort:skip

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
    
    site = f"https://{os.environ.get('site')}"

    expected_string = f"{os.environ.get('expected_string')}"
    
    result = check_website_status(site, expected_string)

    return result