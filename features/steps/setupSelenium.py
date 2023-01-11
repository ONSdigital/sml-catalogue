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
if os.getenv('DEPLOY_URL'):
    print('local_ip = ${env.DEPOLY_URL}')
else:
    local_ip = f"http://{local_ip}:8000/"
