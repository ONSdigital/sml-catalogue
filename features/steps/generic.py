# Step definitions for about page

from urllib.parse import urljoin
import setupSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from behave import *

def document_initialised(driver):
    return driver.execute_script("return initialised")

driver = setupSelenium.driver
host = setupSelenium.local_ip

@given('I\'m an sml portal user')
def auth_user(context):
    driver.get(host)
    WebDriverWait(driver, timeout=10).until(document_initialised)

@when('I navigate to the "{page}" page')
def navigate_to_url(context, page):
    driver.get(urljoin(host + "/resources/", page))


@then('The title of the page is "{title}"')
def check_title(context, title):
    page_title = driver.find_element(By.TAG_NAME, "h1").text
    assert page_title == title
