from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import socket
import os

def returnDriver():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    return driver

def returnWebURL():
    hostname = socket.gethostname()
    website_url = socket.gethostbyname(hostname)

    if os.getenv("deploy_url"):
        website_url = os.getenv('deploy_url')
    else:
        website_url = f"http://{website_url}:8000/"
        
    print("The url selenium is using is: ", website_url)

    return website_url
