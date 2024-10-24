# Step definitions for about page
# pylint: disable=import-error, undefined-variable, unused-argument, function-redefined, duplicate-code

from urllib.parse import urljoin

from setupSelenium import EC, By, WebDriverWait, driver, timeout


@given("I'm an sml portal user")
def auth_user(context):
    driver.get(context.config.userdata.get("host"))
    WebDriverWait(driver, timeout=timeout).until(
        EC.presence_of_element_located((By.ID, "main-title"))
    )


@when('I navigate to the "{page_id}" page')
def navigate_to_page(context, page_id):
    driver.get(urljoin(context.config.userdata.get("host") + "resources/", page_id))
    WebDriverWait(driver, timeout=timeout).until(
        EC.presence_of_element_located((By.ID, "{page_id}-content"))
    )


@when('I navigate to "{url}"')
def navigate_to_url(context, url):
    driver.get(urljoin(context.config.userdata.get("host"), url))
    WebDriverWait(driver, timeout=timeout).until(
        EC.presence_of_element_located((By.ID, "main-content"))
    )


@then('The id of the title is "{id}"')
def check_generic_id(context, id):
    page_id = (
        WebDriverWait(driver, timeout=timeout)
        .until(lambda d: d.find_element(By.ID, "{id}"))
        .id
    )
    assert page_id == id


@then('The subtitle of the page is "{subtitle}"')
def check_subtitle(context, subtitle):
    page_subtitle = (
        WebDriverWait(driver, timeout=10)
        .until(lambda d: d.find_element(By.ID, "page-subtitle"))
        .text
    )
    assert page_subtitle == subtitle
