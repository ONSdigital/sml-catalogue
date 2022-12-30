# Tests for the date thousand pound correction link

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from behave import *
driver = webdriver.Chrome()


@when('I navigate to the thousand pound correction page')
def navigate_to_date_adjustment_method(context):
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, value='ons-card__link').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, value='Thousand pound correction').click()
