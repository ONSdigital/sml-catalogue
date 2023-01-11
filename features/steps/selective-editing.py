# Tests for the selective editing link

import setupSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from behave import *

def document_initialised(driver):
    return driver.execute_script("return initialised")

driver = setupSelenium.driver
host = setupSelenium.local_ip

@given('I\'m an sml portal user trying to get to the selective editing method')
def auth_user(context):
    driver.get(host)
    WebDriverWait(driver, timeout=10).until(document_initialised)

@when('I navigate to the selective editing page')
def navigate_to_date_adjustment_method(context):
    driver.find_element(By.ID, value='title1').click()
    WebDriverWait(driver, timeout=10).until(document_initialised)
    driver.find_element(By.LINK_TEXT, value='Selective Editing').click()
    WebDriverWait(driver, timeout=10).until(document_initialised)


@then('The title of the selective editing page is "{title}"')
def check_title(context, title):
    page_title = driver.find_element(By.TAG_NAME, "h1").text
    assert page_title == title
