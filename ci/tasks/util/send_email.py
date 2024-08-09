import os

from notifications_python_client.notifications import NotificationsAPIClient

templates = {
    "pass": "94772cac-74b6-4b12-afca-11e525e3365a",
    "fail": "45a2acad-7f3b-4993-aac5-2ed618c26787",
    "in_progress": "fd5fb69b-ec9c-408b-b761-5ff11266f50b"
}
firstname = os.environ["FIRSTNAME"]
surname = os.environ["SURNAME"]
email = os.environ["EMAIL"]
api_key = os.environ["GOVNOTIFYAPIKEY"]
state = os.environ["STATUS"]
template = templates[state]

personalisation = {"name": firstname, "surname": surname}
notifications_client = NotificationsAPIClient(api_key)
response = notifications_client.send_email_notification(
    email, template, personalisation
)
print("email sent")
