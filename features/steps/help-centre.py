# Step definitions for help centre page
# pylint: disable=import-error, undefined-variable, unused-argument, function-redefined

from setupSelenium import EC, By, WebDriverWait, driver, timeout


@given("I'm an sml portal user trying to get to the help centre")
def auth_user(context):
    driver.get(context.config.userdata.get("host"))


@given('I\'m an sml portal user on the "{page}" page')
def auth_user(context, page):
    if page == "find and view methods":
        driver.get(
            f'{context.config.userdata.get("host")}help-centre/access/view-methods'
        )
    elif page == "submit a method request":
        driver.get(
            f'{context.config.userdata.get("host")}help-centre/information/methods-request'
        )
    elif page == "coding standards":
        driver.get(
            f'{context.config.userdata.get("host")}help-centre/information/coding-standards'
        )


@when("I navigate to the help centre page")
def navigate_to_url(context):
    WebDriverWait(driver, timeout=timeout).until(
        lambda d: d.find_element(By.LINK_TEXT, value="Help centre")
    ).click()
    WebDriverWait(driver, timeout=timeout).until(
        EC.presence_of_element_located((By.ID, "main-content"))
    )


@when('I click the "{link}" link')
def navigate_to_url(context, link):
    WebDriverWait(driver, timeout=timeout).until(
        lambda d: d.find_element(By.PARTIAL_LINK_TEXT, value=link)
    ).click()


@when("I click the external user dropdown")
def navigate_to_url(context):
    WebDriverWait(driver, timeout=timeout).until(
        lambda d: d.find_element(By.ID, value="collapsibleONSExternalUserId")
    ).click()
    WebDriverWait(driver, timeout=timeout).until(
        EC.presence_of_element_located((By.ID, "collapsibleONSExternalUserId-content"))
    )


@then('The drop down content is "{text}"')
def check_dropdown_title(context, text):
    content_div = WebDriverWait(driver, timeout=timeout).until(
        lambda d: d.find_element(By.ID, value="collapsibleONSExternalUserId-content")
    )
    dropdown_content_elements = content_div.find_elements(By.TAG_NAME, "p")
    dropdown_content = ""

    for element in dropdown_content_elements:
        dropdown_content += element.text
        dropdown_content += " "

    dropdown_content = (
        dropdown_content.replace("(opens in a new tab)", "").replace("\n", "").rstrip()
    )
    assert dropdown_content == text
    


@then('The subtitle of the help centre page is "{subtitle}"')
def check_subtitle(context, subtitle):
    page_title = (
        WebDriverWait(driver, timeout=timeout)
        .until(lambda d: d.find_element(By.LINK_TEXT, subtitle))
        .text
    )
    assert page_title == subtitle
