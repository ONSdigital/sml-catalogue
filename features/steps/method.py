# Step definitions for methods catalogue page

from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from behave import *
driver = webdriver.Chrome()


@given('I\'m an sml portal user trying to get to the methods catalogue page')
def auth_user(context):
    driver.get('http://localhost:5000/')


@when('I navigate to the methods catalogue page')
def navigate_to_url(context):
    driver.find_element(By.ID, value='title1').click()


@then('The title of the methods catalogue page is "{title}"')
def check_title(context, title):
    page_title = driver.find_element(By.TAG_NAME, "h1").text
    assert page_title == title
