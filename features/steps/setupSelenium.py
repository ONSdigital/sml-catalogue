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
if os.getenv('deploy-url'):
    local_ip = f"{os.getenv('deploy-url')}"
else:
    local_ip = f"http://{local_ip}:8000/"
    
print(local_ip)
