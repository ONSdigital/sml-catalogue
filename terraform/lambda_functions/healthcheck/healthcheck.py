import os # isort:skip
import requests # isort:skip

def check_website_status(site):
    timeout = 5

    expected_string = "An open source library for statistical code approved by the ONS"

    try:
        response = requests.get(site, timeout=timeout)

        if response.status_code != 200:
            print(f"site: {site} has a {response.status_code} status code")
            return False
        elif expected_string not in response.text:
            print(f"site: {site} does not contain expected content")
            return False
        
    except Exception as e:
        print(f"Error accessing {site}: {str(e)}")
        return False
        
    return True

def lambda_handler(event, context,):
    
    site = f"https://{os.environ.get('site')}"
    
    result = check_website_status(site)

    return result