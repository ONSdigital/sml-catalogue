import os
import socket
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import socket
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
if os.environ('DEPLOY_URL'):
    local_ip = f"{os.getenv('DEPLOY_URL')}"
else:
    local_ip = f"http://{local_ip}:8000/"

print(local_ip)
