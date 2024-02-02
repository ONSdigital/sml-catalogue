import os # isort:skip
import requests # isort:skip

def check_website_status(urls):
    timeout = 5

    for url in urls:

        try:
            response = requests.get(url, timeout=timeout)

            print(url, response.text)

            if response.status_code != 200:
                print(f"Url: {url} has a {response.status_code} status code")
                return False
            
        except Exception as e:
            print(f"Error accessing {url}: {str(e)}")
            return False
        
    return True

def lambda_handler(event, context,):
    
    websites = os.environ.get("site")
    
    result = check_website_status(websites)

    return result