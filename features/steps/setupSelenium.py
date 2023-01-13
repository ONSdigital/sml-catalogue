import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
if os.getenv('deploy_url'):
    website_url = f"{os.getenv('deploy_url')}"
    website_url = website_url[:-1]
else:
    website_url = "http://127.0.0.1:5000/"
    website_url = website_url[:-1]