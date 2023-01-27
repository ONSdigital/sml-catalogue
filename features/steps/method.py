# Step definitions for methods catalogue page

import setupSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *

driver = setupSelenium.driver
host = setupSelenium.website_url
timeout = setupSelenium.timeout


@given('I\'m an sml portal user trying to get to the methods catalogue page')
def auth_user(context):
    driver.get(host)


@when('I navigate to the methods catalogue page')
def navigate_to_url(context):
     WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.ID, value='title1')).click()
     WebDriverWait(driver, timeout=timeout).until(EC.presence_of_element_located((By.ID, 'collapsible')))


@then('The title of the methods catalogue page is "{title}"')
def check_title(context, title):
    page_title =  WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == title


@given('I am on the methods catalogue page')
def auth_user(context):
    driver.get(f"{host}methods")


@when('I click on the collapsible drop down')
def navigate_to_url(context):
    WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.TAG_NAME, "summary")).click()
    WebDriverWait(driver, timeout=timeout).until(EC.presence_of_element_located((By.ID, 'collapsible-content')))


@then('I see the dropdown content "{text}"')
def check_title(context, text):
    content_div =  WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.ID, value='collapsible-content'))
    dropdown_content_elements = content_div.find_elements(By.TAG_NAME, "p")
    dropdown_content = ""

    for i in range (len(dropdown_content_elements)):
        dropdown_content += dropdown_content_elements[i].text
        dropdown_content += " "

    dropdown_content = dropdown_content.rstrip()
    assert dropdown_content == text


def extractMethodTableContent(context):
    methods_catalogue_table_header = WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_elements(By.CLASS_NAME, "ons-table__header"))

    headers = []
    for header in methods_catalogue_table_header:
        header_button = header.find_element(By.TAG_NAME, "button")
        headers.append(header_button.text)
    

    methods_catalogue_table_rows = WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_elements(By.CLASS_NAME, "ons-table__row"))

    # Come up with a better variable name
    methods = []
    for row in methods_catalogue_table_rows:
        cells = row.find_elements(By.CLASS_NAME, "ons-table__cell")
        new_list = []
        for cell in cells:
            new_list.append(cell.text)
        methods.append(new_list)
    return headers, methods


@then('The table headings of the methods catalogue table are "{name}" "{theme}" "{expertGroup}" "{languages}" "{access}" "{status}"')
def check_methods_catalogue_title(context, name, theme, expertGroup, languages, access, status):
    headers = extractMethodTableContent(context)[0]

    assert name in headers
    assert theme in headers
    assert expertGroup in headers
    assert languages in headers
    assert access in headers
    assert status in headers


@then('The table row of the method are "{name}" "{theme}" "{expertGroup}" "{languages}" "{access}" "{status}"')
def check_methods_catalogue_title(context, name, theme, expertGroup, languages, access, status):
    methods = extractMethodTableContent(context)[1]

    checks = [name, theme, expertGroup, languages, access, status]

    method_found = False
    for method in methods:
        if method == checks:
            method_found = True
    
    assert method_found
