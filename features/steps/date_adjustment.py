# Tests for the date adjustment link

from setupSelenium import returnDriver, returnWebURL
from selenium.webdriver.common.by import By
from behave import *

driver = returnDriver()
host = returnWebURL()


@given('I\'m an sml portal user trying to get to the date adjustment method')
def auth_user(context):
    driver.get(host)
    print("Host: ", host)


@when('I navigate to the date adjustment page')
def navigate_to_date_adjustment_method(context):
    print("Current URL 1: ", driver.current_url)
    test = driver.find_element(By.ID, "main-content")
    print("Current URL 2: ", driver.current_url)
    test_text = test.find_element(By.TAG_NAME, "p").text
    print("Host: ", host)
    print("Test: ", test_text)
    print("Current URL 3: ", driver.current_url)
    driver.find_element(By.ID, value='title1').click()
    driver.find_element(By.LINK_TEXT, value='Date adjustment').click()


@then('The title of the date adjustment page is "{title}"')
def check_title(context, title):
    page_title = driver.find_element(By.TAG_NAME, "h1").text
    print(title, page_title)
    assert page_title == title
