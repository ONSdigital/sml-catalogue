import requests

# Lambda function to check if specified site has the main
# title text and returns the expected status code. 
def lambda_handler(event, context):
    url = 'https://dev-sml.aws.onsdigital.uk/'
    
    try:
        response = requests.get(url)

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