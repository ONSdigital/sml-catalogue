# Step definitions for about page
from urllib.parse import urljoin
import setupSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *

driver = setupSelenium.driver
host = setupSelenium.website_url
timeout = setupSelenium.timeout


@given('I\'m an sml portal user')
def auth_user(context):
    driver.get(host)
    page_title = WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == 'An open source library for statistical code approved by the ONS'


@when('I navigate to the "{page}" page')
def navigate_to_url(context, page):
    driver.get(urljoin(host + "resources/", page))
    WebDriverWait(driver, timeout=timeout).until(EC.presence_of_element_located((By.ID, 'main-content')))


@then('The title of the page is "{title}"')
def check_title(context, title):
    page_title = WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == title

@then('The subtitle of the page is "{subtitle}"')
def check_subtitle(context, subtitle):
    page_subtitle = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, "page-subtitle")).text
    assert page_subtitle == subtitle