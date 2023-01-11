import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
if os.getenv('deploy-url'):
    local_ip = f"{os.getenv('deploy-url')}"
else:
    local_ip = "http://localhost:8000/"
