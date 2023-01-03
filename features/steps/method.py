# Step definitions for methods catalogue page

from selenium import webdriver
from selenium.webdriver.common.by import By
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


@given('I am on the methods catalogue page')
def auth_user(context):
    driver.get('http://localhost:8000/methods')


@when('I click on the collapsible drop down')
def navigate_to_url(context):
    collapsible = driver.find_element(By.ID, value='collapsible')
    collapsible.find_element(By.TAG_NAME, "summary").click()


@then('I see the dropdown content "{text}"')
def check_title(context, text):
    content_div = driver.find_element(By.ID, value='collapsible-content')
    dropdown_content_elements = content_div.find_elements(By.TAG_NAME, "p")
    dropdown_content = ""

    for i in range (len(dropdown_content_elements)):
        dropdown_content += dropdown_content_elements[i].text
        dropdown_content += " "

    dropdown_content = dropdown_content.rstrip()
    assert dropdown_content == text
