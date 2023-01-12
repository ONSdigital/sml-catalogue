# Step definitions for about page
from urllib.parse import urljoin
import setupSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *

driver = setupSelenium.driver
host = setupSelenium.local_ip

@given('I\'m an sml portal user')
def auth_user(context):
    driver.get(host)

@when('I navigate to the "{page}" page')
def navigate_to_url(context, page):
    driver.get(urljoin(host + "/resources/", page))
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, 'main-content')))

@then('The title of the page is "{title}"')
def check_title(context, title):
    page_title = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == title