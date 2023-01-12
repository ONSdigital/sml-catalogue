import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
if os.getenv('deploy_url'):
    website_url = f"{os.getenv('deploy_url')}"
else:
    website_url = "http://localhost:8000/"
