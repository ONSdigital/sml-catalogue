import socket
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
port = 5000