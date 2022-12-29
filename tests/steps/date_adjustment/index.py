# Step definitions for date adjustment page

from lib2to3.pgen2 import driver
import time
from urllib.parse import urljoin
import webbrowser
from pytest_bdd import scenario, given, when, then


@scenario('date_adjustment.feature')
def test_publish():
    pass


@given('I\'m an sml portal user')
def navigate_to_url():
    webbrowser.open('http://127.0.0.1:5000')


@when('I navigate to the date adjustment page')
def navigate_to_url():
    webbrowser.find_element_by_id('title2').click()
    time.sleep(3)
    webbrowser.find_element_by_text('Date adjustment').click()


@then('The title of the page is "Method: Date adjustment"')
def check_title(title):
    assert title in driver.page_source
