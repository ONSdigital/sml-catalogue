# Step definitions for methods catalogue page
# pylint: disable=import-error, undefined-variable, unused-argument, function-redefined, too-many-positional-arguments, redefined-builtin

from setupSelenium import EC, By, WebDriverWait, driver, timeout


@given("I'm an sml portal user trying to get to the methods catalogue page")
def auth_user(context):
    driver.get(context.config.userdata.get("host"))


@when("I navigate to the methods catalogue page")
def navigate_to_url(context):
    WebDriverWait(driver, timeout=timeout).until(
        lambda d: d.find_element(By.ID, value="title1")
    ).click()
    WebDriverWait(driver, timeout=timeout).until(
        EC.presence_of_element_located((By.ID, "collapsible"))
    )


@then('The title of the methods catalogue page is "{title}"')
def check_methods_catalogue_title(context, title):
    page_title = (
        WebDriverWait(driver, timeout=timeout)
        .until(lambda d: d.find_element(By.TAG_NAME, "h1"))
        .text
    )
    assert page_title == title


@given("I am on the methods catalogue page")
def auth_user(context):
    driver.get(f'{context.config.userdata.get("host")}methods/index')


@when("I click on the collapsible drop down")
def navigate_to_url(context):
    WebDriverWait(driver, timeout=timeout).until(
        lambda d: d.find_element(By.ID, "collapsible")
    ).click()
    WebDriverWait(driver, timeout=timeout).until(
        EC.presence_of_element_located((By.ID, "collapsible"))
    )


@then('The id of the dropdown is "{id}"')
def check_dropdown_id(context, id):
    dropdown_content_id = (
        WebDriverWait(driver, timeout=timeout)
        .until(lambda d: d.find_element(By.ID, id))
        .get_attribute("id")
    )
    assert dropdown_content_id == id


def extractMethodTableContent(context, table):
    methods_catalogue_table = WebDriverWait(driver, timeout=timeout).until(
        lambda d: d.find_element(By.ID, value=f"{table}-table")
    )
    methods_catalogue_table_header = methods_catalogue_table.find_elements(
        By.CLASS_NAME, "ons-table__header"
    )

    headers = []
    for header in methods_catalogue_table_header:
        header_button = header.find_element(By.TAG_NAME, "button")
        headers.append(header_button.text)

    methods_catalogue_table_rows = WebDriverWait(driver, timeout=timeout).until(
        lambda d: d.find_elements(By.CLASS_NAME, "ons-table__row")
    )

    methods = []
    for row in methods_catalogue_table_rows:
        cells = row.find_elements(By.CLASS_NAME, "ons-table__cell")
        new_list = []
        for cell in cells:
            new_list.append(cell.text)
        methods.append(new_list)
    return headers, methods


@then(
    'The "{table}" table headings of the methods catalogue table are "{name}" "{theme}" "{expertGroup}" "{languages}"'
)
def check_methods_catalogue_title(context, table, name, theme, expertGroup, languages):
    headers = extractMethodTableContent(context, table)[0]

    assert name in headers
    assert theme in headers
    assert expertGroup in headers
    assert languages in headers


@then(
    'The "{table}" table row of the method are "{name}" "{theme}" "{expertGroup}" "{languages}"'
)
def check_methods_catalogue_title(context, table, name, theme, expertGroup, languages):
    methods = extractMethodTableContent(context, table)[1]

    checks = [name, theme, expertGroup, languages]

    method_found = False
    for method in methods:
        if method == checks:
            method_found = True

    assert method_found
