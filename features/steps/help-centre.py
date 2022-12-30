# Step definitions for help centre page

from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from behave import *
driver = webdriver.Chrome()


@given('I\'m an sml portal user trying to get to the help centre')
def auth_user(context):
    driver.get('http://localhost:5000/')


@when('I navigate to the help centre page')
def navigate_to_url(context):
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, value='Help centre').click()


@then('The title of the help centre page is "{title}"')
def check_title(context, title):
    main_content = driver.find_element(By.ID, value="main-content")
    page_title = main_content.find_element(By.TAG_NAME, value="h1").text
    assert page_title == title
