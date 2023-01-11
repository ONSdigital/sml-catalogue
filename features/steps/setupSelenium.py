from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import socket
import os
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

# hostname = socket.gethostname()
# website_url = socket.gethostbyname(hostname)

website_url = os.getenv("env.deploy_url")
# website_url = f"http://{website_url}:8000"
