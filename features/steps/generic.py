# Step definitions for about page

from urllib.parse import urljoin
import setupSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from behave import *

driver = setupSelenium.driver
host = setupSelenium.local_ip

@given('I\'m an sml portal user')
def auth_user(context):
    WebDriverWait(driver, timeout=10).until(host)

@when('I navigate to the "{page}" page')
def navigate_to_url(context, page):
    WebDriverWait(driver, timeout=10).until(urljoin(host + "/resources/", page))


@then('The title of the page is "{title}"')
def check_title(context, title):
    page_title = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == title
