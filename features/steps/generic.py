# Step definitions for about page

import os
from urllib.parse import urljoin
import setupSelenium
from selenium.webdriver.common.by import By
from behave import *

driver = setupSelenium.driver


@given('I\'m an sml portal user')
def auth_user(context):
    driver.get(os.environ.get('DEPLOY_URL'))


@when('I navigate to the "{page}" page')
def navigate_to_url(context, page):
    driver.get(urljoin(os.environ.get('DEPLOY_URL'), f'resources/{page}'))


@then('The title of the page is "{title}"')
def check_title(context, title):
    page_title = driver.find_element(By.TAG_NAME, "h1").text
    assert page_title == title
