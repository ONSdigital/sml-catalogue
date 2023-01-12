# Tests for the ht/ratio estimation link

import setupSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *

driver = setupSelenium.driver
host = setupSelenium.local_ip

@given('I\'m an sml portal user trying to get to the ht/ratio estimation method')
def auth_user(context):
    driver.get(host)
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, 'title1')))

@when('I navigate to the ht/ratio estimation page')
def navigate_to_date_adjustment_method(context):
     WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, value='title1')).click()
     WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.LINK_TEXT, value='HT/Ratio Estimation')).click()


@then('The title of the ht/ratio estimation page is "{title}"')
def check_title(context, title):
    page_title =  WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == title
