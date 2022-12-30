# Step definitions for help center page

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from behave import *
driver = webdriver.Chrome()


@when('I navigate to the help center page')
def navigate_to_url(context):
    driver.find_element(By.ID, value='title2').click()
