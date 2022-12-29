# Step definitions for methods catalogue page

from lib2to3.pgen2 import driver
from urllib.parse import urljoin
import webbrowser
from pytest_bdd import scenario, given, when, then


@scenario('methods.feature')
def test_publish():
    pass


@given('I\'m an sml portal user')
def navigate_to_url():
    webbrowser.open('http://127.0.0.1:5000')


@when('I am on the methods catalogue page')
def navigate_to_url():
    webbrowser.find_element_by_id('title2').click()


@then('The title of the page is "All methods"')
def check_title(title):
    assert title in driver.page_source
