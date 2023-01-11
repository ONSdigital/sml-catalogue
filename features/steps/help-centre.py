# Step definitions for help centre page

import setupSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from behave import *

def document_initialised(driver):
    return driver.execute_script("return initialised")

driver = setupSelenium.driver
host = setupSelenium.local_ip

@given('I\'m an sml portal user trying to get to the help centre')
def auth_user(context):
    driver.get(host)
    WebDriverWait(driver, timeout=10).until(document_initialised)

@when('I navigate to the help centre page')
def navigate_to_url(context):
    driver.find_element(By.LINK_TEXT, value='Help centre').click()
    WebDriverWait(driver, timeout=10).until(document_initialised)


@then('The title of the help centre page is "{title}"')
def check_title(context, title):
    page_title = driver.find_element(By.TAG_NAME, value="h1").text
    assert page_title == title
