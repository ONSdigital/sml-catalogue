import os # isort:skip
import requests # isort:skip
from bs4 import BeautifulSoup # isort:skip

def check_website_status(site):
    timeout = 5

    try:
        response = requests.get(site, timeout=timeout)

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the title of the page
        title = soup.title.text.strip()

        print(title)

        if response.status_code != 200:
            print(f"site: {site} has a {response.status_code} status code")
            return False
        
    except Exception as e:
        print(f"Error accessing {site}: {str(e)}")
        return False
        
    return True

def lambda_handler(event, context,):
    
    site = f"https://{os.environ.get('site')}"
    
    result = check_website_status(site)

    return result