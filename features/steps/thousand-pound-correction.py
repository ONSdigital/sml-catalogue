# Tests for the thousand pound correction link

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from behave import *
driver = webdriver.Chrome()


@given('I\'m an sml portal user trying to get to the thousand pound correction method')
def auth_user(context):
    driver.get('http://localhost:5000/')


@when('I navigate to the thousand pound correction page')
def navigate_to_date_adjustment_method(context):
    time.sleep(1)
    driver.find_element(By.ID, value='title1').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, value='Thousand pound correction').click()


@then('The title of the thousand pound correction page is "{title}"')
def check_title(context, title):

    main_content = driver.find_element(By.ID, value="main-content")
    page_title = main_content.find_element(By.TAG_NAME, "h1").text
    assert page_title == title
