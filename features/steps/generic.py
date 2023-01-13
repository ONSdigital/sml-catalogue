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
    driver.get("https://d1jgbw8ee9pybj.cloudfront.net/")
    page_title = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    print('Discover methods used by the Office for National Statistics')
    print(page_title)
    assert page_title == 'Discover methods used by the Office for National Statistics'

@when('I navigate to the "{page}" page')
def navigate_to_url(context, page):
    print('host: ', host)
    driver.get(urljoin(host + "resources/", page))
    print(urljoin(host + "resources/", page))
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, 'main-content')))

@then('The title of the page is "{title}"')
def check_title(context, title):
    page_title = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    print(title)
    print(page_title)
    assert page_title == title

