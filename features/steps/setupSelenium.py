from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from axe_selenium_python import Axe
from behave import *

# For local testing use the host local host

options = Options()
options.headless = True
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)
# host = "https://statisticalmethodslibrary.ons.gov.uk/" # prod
# host = "https://preprod-sml.aws.onsdigital.uk/" # preprod
host = "https://d1jgbw8ee9pybj.cloudfront.net/" # dev
# host = "http://localhost:8000/"
timeout = 5
