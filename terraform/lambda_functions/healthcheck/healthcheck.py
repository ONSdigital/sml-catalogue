import requests # isort:skip

# Lambda function to check if specified site has the main
# title text and returns the expected status code. 
def lambda_handler(event, context):
    urls_to_check = ['https://dev-sml.aws.onsdigital.uk/', 'https://preprod-sml.aws.onsdigital.uk/', 'https://statisticalmethodslibrary.ons.gov.uk/']
    timeout = 5
    
    for url in urls_to_check:
        try:
            response = requests.get(url, timeout=timeout)


            verify_text = 'An open source library for statistical code approved by the ONS'
            if verify_text in response.text:
                result = {
                    'statusCode': response.status_code,
                    'body': f'"{url}" is healthy'
                }
            else:
                result = {
                    'statusCode': response.status_code,
                    'body': f'"{url}" is not healthy'
                }

        except requests.RequestException as e:
            result = {
                'statusCode': 500,
                'body': f'Request error: {str(e)}'
            }

    return result