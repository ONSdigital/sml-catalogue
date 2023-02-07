from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
website_url = "http://127.0.0.1:5000/"
timeout = 5