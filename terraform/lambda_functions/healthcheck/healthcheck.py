import requests # isort:skip

def check_website_status(urls):
    for url in urls:

        try:
            response = requests.get(url)

            if response.status_code != 200:
                print(f"Url: {url} has a {response.status_code} status code")
                return False
            
        except Exception as e:
            print(f"Error accessing {url}: {str(e)}")
            return False
        
    return True

def lambda_handler(event, context):
    
    websites = ['https://dev-sml.aws.onsdigital.uk', 'https://preprod-sml.aws.onsdigital.uk', 'https://statisticalmethodslibrary.ons.gov.uk']
    
    result = check_website_status(websites)

    return result