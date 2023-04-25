from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
host = "https://statisticalmethodslibrary.ons.gov.uk"
timeout = 5
