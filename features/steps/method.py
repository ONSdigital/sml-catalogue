# Step definitions for methods catalogue page

from urllib.parse import urljoin
import setupSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from behave import *
import time

driver = setupSelenium.driver
host = setupSelenium.local_ip

@given('I\'m an sml portal user trying to get to the methods catalogue page')
def auth_user(context):
    driver.get(host)

@when('I navigate to the methods catalogue page')
def navigate_to_url(context):
     WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, value='title1')).click()


@then('The title of the methods catalogue page is "{title}"')
def check_title(context, title):
    page_title =  WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == title


@given('I am on the methods catalogue page')
def auth_user(context):
    driver.get(host + "/methods/")


@when('I click on the collapsible drop down')
def navigate_to_url(context):
    collapsible =  WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, value='collapsible'))
    collapsible.find_element(By.TAG_NAME, "summary").click()


@then('I see the dropdown content "{text}"')
def check_title(context, text):
    content_div =  WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, value='collapsible-content'))
    dropdown_content_elements = content_div.find_elements(By.TAG_NAME, "p")
    dropdown_content = ""

    for i in range (len(dropdown_content_elements)):
        dropdown_content += dropdown_content_elements[i].text
        dropdown_content += " "

    dropdown_content = dropdown_content.rstrip()
    assert dropdown_content == text
