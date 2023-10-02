# pylint: disable=wildcard-import, unused-import, unused-wildcard-import

# F401 We have to import the modules below here and they get
# used in other files later on so ignoring this F401 error
from axe_selenium_python import Axe  # noqa: F401
from behave import *  # noqa: F401
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # noqa: F401
from selenium.webdriver.support import expected_conditions as EC  # noqa: F401
from selenium.webdriver.support.wait import WebDriverWait  # noqa: F401

options = Options()
options.headless = True
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=options)
timeout = 5
