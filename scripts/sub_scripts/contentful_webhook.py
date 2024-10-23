import os
import sys

from contentful_management import Client

CDA_KEY = os.environ.get("CLI_KEY")
SPACE_ID = os.environ.get("SPACE_ID")
ACTIVE_VALUE = os.environ.get("ACTIVE_VALUE")
client = Client(CDA_KEY)

webhooks = client.webhooks(SPACE_ID).find("4pAWhYZSUHT8wNyzW6fff8")
webhooks.update({"active": ACTIVE_VALUE == "True"})

webhooks = client.webhooks(SPACE_ID).find("4pAWhYZSUHT8wNyzW6fff8")
output = webhooks.__dict__
if str(output["raw"]["active"]) != ACTIVE_VALUE:
    sys.exit("Webhook active status does not match intended value. Exiting.")
