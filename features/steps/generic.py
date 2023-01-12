# Step definitions for about page
from urllib.parse import urljoin
import setupSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *

driver = setupSelenium.driver
host = setupSelenium.website_url

@given('I\'m an sml portal user')
def auth_user(context):
    driver.get(host)

@when('I navigate to the "{page}" page')
def navigate_to_url(context, page):
    print('host: ', host)
    driver.get(urljoin(host + "resources/", page))
    print(urljoin(host + "resources/", page))
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, 'main-content')))

@then('The title of the page is "{title}"')
def check_title(context, title):
    page_title = driver.FindElement(By.ID('h1'))
    print(driver.current_url)
    print(title)
    print(page_title)
    assert page_title == title

