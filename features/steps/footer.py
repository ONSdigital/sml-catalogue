# Tests for the date adjustment link
# pylint: disable=import-error, undefined-variable, unused-argument, function-redefined

from setupSelenium import EC, By, WebDriverWait, driver, timeout


@given('I\'m an sml portal user trying to get to the "{page}" page')
def auth_user(context, page):
    driver.get(context.config.userdata.get("host"))


@when('I click the "{page}" page on the footer')
def navigate_to_url(context, page):
    WebDriverWait(driver, timeout=timeout).until(
        lambda d: d.find_element(By.LINK_TEXT, value=page)
    ).click()
    WebDriverWait(driver, timeout=timeout).until(
        EC.presence_of_element_located((By.ID, "main-content"))
    )


@then('The title of page is "{title}"')
def check_title(context, title):
    page_title = (
        WebDriverWait(driver, timeout=timeout)
        .until(lambda d: d.find_element(By.TAG_NAME, "h1"))
        .text
    )
    assert page_title == title
