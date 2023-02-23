# Tests for the date adjustment link

from setupSelenium import *


@given('I\'m an sml portal user trying to get to the "{method}" summary page')
def auth_user(context, method):
    driver.get(host)


@when('I navigate to the "{method}" summary page')
def navigate_to_the_method(context, method):
    WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.ID, value='title1')).click()
    WebDriverWait(driver, timeout=timeout).until(EC.presence_of_element_located((By.ID, 'collapsible')))
    WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.LINK_TEXT, value=method)).click()
    WebDriverWait(driver, timeout=timeout).until(EC.presence_of_element_located((By.ID, 'main-content')))


@then('The title of the method summary page is "{title}"')
def check_title(context, title):
    page_title = WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == title
