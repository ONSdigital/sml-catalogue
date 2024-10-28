# Step definitions for about page
# pylint: disable=import-error, undefined-variable, unused-argument, function-redefined, duplicate-code, redefined-builtin

from urllib.parse import urljoin

from setupSelenium import EC, By, WebDriverWait, driver, timeout


@given("I'm an sml portal user")
def auth_user(context):
    driver.get(context.config.userdata.get("host"))
    WebDriverWait(driver, timeout=timeout).until(
        EC.presence_of_element_located((By.ID, "main-title"))
    )


@when("The page loads")
def page_loads(context):
    WebDriverWait(driver, timeout=timeout).until(
        EC.presence_of_element_located((By.ID, "title1"))
    )


@when('I navigate to "{url}"')
def navigate_to_url(context, url):
    driver.get(urljoin(context.config.userdata.get("host"), url))
    WebDriverWait(driver, timeout=timeout).until(
        EC.presence_of_element_located((By.ID, "main-content"))
    )


@then('The verified id is "{id}"')
def check_generic_title_id(context, id):
    verify_id = (
        WebDriverWait(driver, timeout=timeout)
        .until(lambda d: d.find_element(By.ID, id))
        .get_attribute("id")
    )
    print(verify_id)
    assert verify_id == id


@then('The title of the page is "{title}"')
def check_title(context, title):
    page_title = (
        WebDriverWait(driver, timeout=10)
        .until(lambda d: d.find_element(By.TAG_NAME, "h1"))
        .text
    )
    assert page_title == title
