# Tests for the date adjustment link

import setupSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *

driver = setupSelenium.driver
host = setupSelenium.website_url

@given('I\'m an sml portal user on the home page with a cookie banner')
def auth_user(context):
    driver.delete_all_cookies()
    driver.get(host)
    page_title = WebDriverWait(driver, timeout=40).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == 'Discover methods used by the Office for National Statistics'

@when('I click the accept cookies button in the header')
def auth_user(context):
    WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME, value='ons-js-accept-cookies')).click()

@when('I click the reject cookies button in the header')
def auth_user(context):
    WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME, value='ons-js-reject-cookies')).click()

@when('I click the additional cookies link in the header')
def auth_user(context):
    WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.PARTIAL_LINK_TEXT, value='additional cookies')).click()

@when('I click the view cookies link in the header')
def auth_user(context):
    WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.LINK_TEXT, value='View cookies')).click()

@then('The cookie banner displays "{title}"')
def auth_cookie(context, title):
    page_title =  WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME, value='ons-cookies-banner__desc')).text
    assert page_title == title

@then('I am taken to the "{title}" page')
def check_title(context, title):
    page_title =  WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == title