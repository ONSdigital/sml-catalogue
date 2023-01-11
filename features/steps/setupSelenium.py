from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import socket
import os
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

hostname = socket.gethostname()
website_url = socket.gethostbyname(hostname)

if os.getenv("deploy_url"):
    website_url = f"{os.getenv('deploy_url')}"
else:
    website_url = f"http://{website_url}:8000/"

print("The url selenium is using is: ", website_url)
