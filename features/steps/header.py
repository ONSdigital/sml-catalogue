# Step definitions for methods catalogue page

import setupSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from behave import *

def document_initialised(driver):
    return driver.execute_script("return initialised")

driver = setupSelenium.driver
host = setupSelenium.local_ip

@given('I\'m an sml portal user on the home page')
def auth_user(context):
    driver.get(host)
    
@when('I click the "{page}" link in the header')
def navigate_to_url(context, page):
    if page == "methods catalogue":
        main_navigation = driver.find_element(By.ID, value='main-navigation')
        main_navigation.find_element(By.LINK_TEXT, value='Methods catalogue').click()
        WebDriverWait(driver, timeout=10).until(document_initialised)
    elif page == "help centre":
        main_navigation = driver.find_element(By.ID, value='main-navigation')
        main_navigation.find_element(By.LINK_TEXT, value='Help centre').click()
        WebDriverWait(driver, timeout=10).until(document_initialised)


@then('The title of this page is "{title}"')
def check_title(context, title):
    page_title = driver.find_element(By.TAG_NAME, "h1").text
    assert page_title == title
