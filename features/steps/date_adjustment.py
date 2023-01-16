# Tests for the date adjustment link

from setupSelenium import returnDriver
from selenium.webdriver.common.by import By
from behave import *

driver = returnDriver()
# host = returnWebURL()


@given('I\'m an sml portal user trying to get to the date adjustment method')
def auth_user(context):
    print("Current URL 1: ", driver.current_url)
    driver.get("https://d273a4m6g1cakm.cloudfront.net")
    print("Current URL 2: ", driver.current_url)
    # print("Host: ", host)


@when('I navigate to the date adjustment page')
def navigate_to_date_adjustment_method(context):
    print("Current URL 3: ", driver.current_url, driver.title)
    test = driver.find_element(By.ID, "main-content")
    print("Current URL 4: ", driver.current_url, driver.title)
    test_text = test.find_element(By.TAG_NAME, "p").text
    print("Current URL 5: ", driver.current_url, driver.title)
    # print("Host: ", host)
    print("Test: ", test_text)
    print("Current URL 6: ", driver.current_url, driver.title)
    driver.find_element(By.ID, value='title1').click()
    print("Current URL 7: ", driver.current_url, driver.title)
    driver.find_element(By.LINK_TEXT, value='Date adjustment').click()
    print("Current URL 8: ", driver.current_url, driver.title)


@then('The title of the date adjustment page is "{title}"')
def check_title(context, title):
    page_title = driver.find_element(By.TAG_NAME, "h1").text
    print(title, page_title)
    assert page_title == title
