from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from axe_selenium_python import Axe
from behave import *
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
host = "http://localhost:8000/"
timeout = 5
