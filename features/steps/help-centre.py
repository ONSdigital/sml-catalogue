# Step definitions for help centre page

import setupSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *

driver = setupSelenium.driver
host = setupSelenium.website_url

@given('I\'m an sml portal user trying to get to the help centre')
def auth_user(context):
    driver.get(host)

@when('I navigate to the help centre page')
def navigate_to_url(context):
     WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.LINK_TEXT, value='Help centre')).click()
     WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, 'main-content')))

@then('The title of the help centre page is "{title}"')
def check_title(context, title):
    page_title =  WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.TAG_NAME, value="h1")).text
    assert page_title == title

@then('The subtitle of the help centre page is "{subtitle}"')
def check_title(context, subtitle):
    page_title =  WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.LINK_TEXT, subtitle)).text
    assert page_title == subtitle