# Tests for the selective editing link

import setupSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *

driver = setupSelenium.driver
host = setupSelenium.local_ip

@given('I\'m an sml portal user trying to get to the selective editing method')
def auth_user(context):
    driver.get(host)

@when('I navigate to the selective editing page')
def navigate_to_date_adjustment_method(context):
    WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, value='title1')).click()
    WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.LINK_TEXT, value='Selective Editing')).click()


@then('The title of the selective editing page is "{title}"')
def check_title(context, title):
    page_title = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == title
