# Step definitions for about page

from urllib.parse import urljoin
import setupSelenium
from selenium.webdriver.common.by import By
from behave import *

driver = setupSelenium.driver
host = setupSelenium.local_ip
port = setupSelenium.port

@given('I\'m an sml portal user')
def auth_user(context):
    driver.get(f"{host}:{port}/")


@when('I navigate to the "{page}" page')
def navigate_to_url(context, page):
    driver.get(urljoin(f"{host}:{port}/", f'resources/{page}'))


@then('The title of the page is "{title}"')
def check_title(context, title):
    page_title = driver.find_element(By.TAG_NAME, "h1").text
    assert page_title == title
