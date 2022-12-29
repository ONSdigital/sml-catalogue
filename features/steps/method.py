# Tests for the methods catalogue link

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from behave import *
driver = webdriver.Chrome()


@given('I\'m an sml portal user')
def auth_user(context):
    driver.get('http://localhost:5000/')


@when('I navigate to the methods catalogue page')
def navigate_to_url(context):
    driver.find_element(By.ID, 'title1').click()


@then('The title of the page is "{title}"')
def check_title(context, title):

    main_content = driver.find_element(By.ID, value="main-content")
    page_title = main_content.find_element(By.TAG_NAME, "h1").text
    assert page_title == title
