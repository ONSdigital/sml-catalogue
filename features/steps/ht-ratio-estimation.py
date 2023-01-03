# Tests for the ht/ratio estimation link

from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import *
driver = webdriver.Chrome()


@given('I\'m an sml portal user trying to get to the ht/ratio estimation method')
def auth_user(context):
    driver.get('http://localhost:8000/')


@when('I navigate to the ht/ratio estimation page')
def navigate_to_date_adjustment_method(context):
    driver.find_element(By.ID, value='title1').click()
    driver.find_element(By.LINK_TEXT, value='HT/Ratio Estimation').click()


@then('The title of the ht/ratio estimation page is "{title}"')
def check_title(context, title):
    page_title = driver.find_element(By.TAG_NAME, "h1").text
    assert page_title == title
