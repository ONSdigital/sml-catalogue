import os # isort:skip
import requests # isort:skip

def check_website_status(site):
    timeout = 5

    expected_string = "An open source library for statistical code approved by the ONS"

    try:
        response = requests.get(site, timeout=timeout)

        if response.status_code != 200:
            return False
        elif expected_string not in response.text:
            return False
        
    except Exception as e:
        print(f"Error accessing {site}: {str(e)}")
        return False
        
    return True

def lambda_handler(event, context,):
    
    site = f"https://{os.environ.get('site')}"
    
    result = check_website_status(site)

    if result:
        print(f"site: {site} is live and working")
    else:
        print(f"site: {site} has an issue")

    return result