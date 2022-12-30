# Tests for the methods catalogue link

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from behave import *
driver = webdriver.Chrome()


@when('I navigate to the methods catalogue page')
def navigate_to_methods(context):
    time.sleep(1)
    driver.find_element(By.ID, value='title1').click()
