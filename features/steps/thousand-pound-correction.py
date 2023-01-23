# Tests for the thousand pound correction link

import setupSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *

driver = setupSelenium.driver
host = setupSelenium.website_url

@given('I\'m an sml portal user trying to get to the thousand pound correction method')
def auth_user(context):
    driver.get(host)

@when('I navigate to the thousand pound correction page')
def navigate_to_thousand_pound_method(context):
    WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, value='title1')).click()
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, 'collapsible')))
    WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.LINK_TEXT, value='Thousand pound correction')).click()
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, 'main-content')))


@then('The title of the thousand pound correction page is "{title}"')
def check_title(context, title):
    page_title = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == title
