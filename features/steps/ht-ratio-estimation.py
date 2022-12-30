# Tests for the ht/ratio estimation link

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from behave import *
driver = webdriver.Chrome()


@when('I navigate to the ht/ratio estimation page')
def navigate_to_date_adjustment_method(context):
    time.sleep(1)
    driver.find_element(By.ID, value='Methods catalogue').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, value='HT/Ratio Estimation').click()
