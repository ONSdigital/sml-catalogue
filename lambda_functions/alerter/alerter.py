import json
import os

import requests


def lambda_handler(event, context):
    """
    lambda_handler The purpose of this lambda function is to alert the sml-portal-alert
    slack channel if an alarm is failing (failing alarm triggers lambda)

    :param event: General Lambda term (not used in this case but needed for general setup).
    :type event: N/A
    :param context: General Lambda term (not used in this case but needed for general setup).
    :type context: N/A
    :return: Return a success or failure outcome on whether the slack message was sent.
    :rtype: json
    :raises Exeption: will raise a runtime error if the post fails to send.
    :raises Exeption: error
    """

    # Get the needed variables
    lambda_name = os.environ.get("lambda_name")
    alarm_name = os.environ.get("alarm_name")
    url = os.environ.get("url")
    # The slack token is formed here to push the message to the correct channel
    slack_url_prefix = os.environ.get("slack_url")
    slack_webhook_token = os.environ.get("slack_webhook_token")
    slack_webhook_url = f"{slack_url_prefix}/{slack_webhook_token}"

    # Message sent to channel
    alert_message = {
        "Summary": f"The website at {url} is unreachable. Healthcheck failure.",
        "Alarm": "Route53 Health Check Failure.",
        "Description": f"Website is unreachable or not returning the expected response. Check Amazon Cloudwatch Alarms \'{alarm_name}\' and Healthcheck Lambda \'{lambda_name}\'.",
    }

    try:
        # Send the request
        requests.post(
            slack_webhook_url,
            timeout=5,
            data=json.dumps(alert_message),
            headers={"Content-Type": "application/json"},
        )

        return {
            "statusCode": 200,
            "body": json.dumps("Message sent to Slack successfully."),
        }
    except Exception as e:
        raise RuntimeError(f"Error sending message to Slack: {e}.") from None
