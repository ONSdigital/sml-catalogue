# pylint: disable=wildcard-import, unused-import, unused-wildcard-import

from axe_selenium_python import Axe
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.headless = True
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=options)
timeout = 5
