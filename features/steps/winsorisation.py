# Tests for the winsorisation link

import setupSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from behave import *

driver = setupSelenium.driver
host = setupSelenium.local_ip

@given('I\'m an sml portal user trying to get to the winsorisation method')
def auth_user(context):
    driver.get(f"{host}methods")
    
@when('I navigate to the winsorisation page')
def navigate_to_date_adjustment_method(context):
    WebDriverWait(driver, timeout=20).until(lambda d: d.find_element(By.LINK_TEXT, value='Winsorisation')).click()


@then('The title of the winsorisation page is "{title}"')
def check_title(context, title):
    page_title = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == title
