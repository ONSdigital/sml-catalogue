import os

from notifications_python_client.notifications import NotificationsAPIClient

firstname = os.environ["FIRSTNAME"]
surname = os.environ["SURNAME"]
email = os.environ["EMAIL"]
api_key = os.environ["GOVNOTIFYAPIKEY"]
end_state = os.environ["STATUS"]
template = (
    "94772cac-74b6-4b12-afca-11e525e3365a"
    if end_state == "pass"
    else "45a2acad-7f3b-4993-aac5-2ed618c26787"
)
personalisation = {"name": firstname, "surname": surname}
print(f'values are {firstname} {surname} {email} {end_state} {template}')
notifications_client = NotificationsAPIClient(api_key)
response = notifications_client.send_email_notification(
    email, template, personalisation
)
print(response)
print("email sent")
