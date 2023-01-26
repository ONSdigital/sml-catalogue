# Tests for the cookie preferences

import setupSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *

driver = setupSelenium.driver
host = setupSelenium.website_url
timeout = setupSelenium.timeout


@given('I\'m an sml portal user on the home page with a cookie banner')
def auth_user_home_page(context):
    driver.delete_all_cookies()
    driver.get(host)
    banner = WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert banner == 'Discover methods used by the Office for National Statistics'


@given('I am on the cookies page')
def auth_user_cookie_page(context):
    driver.delete_all_cookies()
    driver.get(f"{host}cookies")
    page_title = WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == 'Cookies on the statistical methods library portal'


@given('I am on the cookies page where cookies are already enabled')
def auth_user_cookie_page_cookies_enabled(context):
    driver.delete_all_cookies()
    driver.get(f"{host}cookies")
    WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.CLASS_NAME, value='ons-js-accept-cookies')).click()


@given('I am on the cookies page where cookies are already disabled')
def auth_user_cookie_page_cookies_disabled(context):
    driver.delete_all_cookies()
    driver.get(f"{host}cookies")
    WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.CLASS_NAME, value='ons-js-reject-cookies')).click()


@when('I click the accept cookies button in the header')
def click_accept_button(context):
    WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.CLASS_NAME, value='ons-js-accept-cookies')).click()


@when('I click the reject cookies button in the header')
def click_reject_button(context):
    WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.CLASS_NAME, value='ons-js-reject-cookies')).click()


@when('I click the additional cookies link in the header')
def navigate_to_cookie_page_via_additional_cookies_link(context):
    WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.PARTIAL_LINK_TEXT, value='additional cookies')).click()


@when('I click the view cookies link in the header')
def navigate_to_cookie_page_via_view_cookies_link(context):
    WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.LINK_TEXT, value='View cookies')).click()


@when('I click the cookie page drop down')
def click_dropdown(context):
    WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.TAG_NAME, "summary")).click()
    WebDriverWait(driver, timeout=timeout).until(EC.presence_of_element_located((By.ID, 'cookies-essential-details')))


@when('I change my settings to enable cookies')
def enable_cookie(context):
    WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.ID, "on-3-label")).click()
    WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.ID, "ons_cookie_save_changes")).click()
    WebDriverWait(driver, timeout=timeout).until(EC.presence_of_element_located((By.ID, 'alert')))


@when('I change my settings to disable cookies')
def disable_cookie(context):
    WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.ID, "off-3-label")).click()
    WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.ID, "ons_cookie_save_changes")).click()
    WebDriverWait(driver, timeout=timeout).until(EC.presence_of_element_located((By.ID, 'alert')))


@then('The cookie banner displays "{banner}"')
def cookie_banner_check(context, banner):
    page_banner =  WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.CLASS_NAME, value='ons-cookies-banner__desc')).text
    assert page_banner == banner


@then('I am taken to the "{title}" page')
def check_title_for_cookie_page(context, title):
    page_title =  WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == title


@then('I see the cookie drop down content "{content}"')
def check_content_for_dropdown(context, content):
    content_div =  WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.ID, value='cookies-essential-details-content'))
    dropdown_content_elements = content_div.find_elements(By.TAG_NAME, "h4")
    dropdown_content = ""

    for i in range (len(dropdown_content_elements)):
        dropdown_content += dropdown_content_elements[i==0].text

    dropdown_content = dropdown_content.rstrip().replace('Cookie message', '')
    assert dropdown_content == content


@then('The cookies are enabled')
def cookie_enabled_check(context):
    alert_content = WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.ID, "cookie_change_alert")).text
    assert alert_content == 'Your cookie settings have been saved'


@then('The cookies are disabled')
def cookie_disabled_check(context):
    alert_content = WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.ID, "cookie_change_alert")).text
    assert alert_content == 'Your cookie settings have been saved'
