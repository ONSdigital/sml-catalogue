# Tests for the date adjustment link

import setupSelenium
from selenium.webdriver.common.by import By
from behave import *

driver = setupSelenium.driver


@given('I\'m an sml portal user trying to get to the date adjustment method')
def auth_user(context):
    driver.get('https://dka5cqmdre2ci.cloudfront.net/')


@when('I navigate to the date adjustment page')
def navigate_to_date_adjustment_method(context):
    driver.find_element(By.ID, value='title1').click()
    driver.find_element(By.LINK_TEXT, value='Date adjustment').click()


@then('The title of the date adjustment page is "{title}"')
def check_title(context, title):
    page_title = driver.find_element(By.TAG_NAME, "h1").text
    assert page_title == title
