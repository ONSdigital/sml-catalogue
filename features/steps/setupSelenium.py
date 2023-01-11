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
local_ip = f"http://{local_ip}:8000/"
for name, value in os.environ.items():
    print("{0}: {1}".format(name, value))
