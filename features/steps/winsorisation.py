# Tests for the winsorisation link

from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import *
driver = webdriver.Chrome()


@given('I\'m an sml portal user trying to get to the winsorisation method')
def auth_user(context):
    driver.get('http://localhost:8000/')


@when('I navigate to the winsorisation page')
def navigate_to_date_adjustment_method(context):
    driver.find_element(By.ID, value='title1').click()
    driver.find_element(By.LINK_TEXT, value='Winsorisation').click()


@then('The title of the winsorisation page is "{title}"')
def check_title(context, title):
    page_title = driver.find_element(By.TAG_NAME, "h1").text
    assert page_title == title
