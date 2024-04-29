# Tests for the date adjustment link
# pylint: disable=import-error, undefined-variable, unused-argument, function-redefined, duplicate-code

from setupSelenium import EC, By, WebDriverWait, driver, timeout


@given('I\'m an sml portal user trying to get to the "{method}" summary page')
def auth_user(context, method):
    driver.get(context.config.userdata.get("host"))


@when('I navigate to the "{method}" summary page')
def navigate_to_the_method(context, method):
    WebDriverWait(driver, timeout=timeout).until(
        lambda d: d.find_element(By.ID, value="title1")
    ).click()
    WebDriverWait(driver, timeout=timeout).until(
        EC.presence_of_element_located((By.ID, "collapsible"))
    )
    WebDriverWait(driver, timeout=timeout).until(
        lambda d: d.find_element(By.LINK_TEXT, value=method)
    ).click()
    WebDriverWait(driver, timeout=timeout).until(
        EC.presence_of_element_located((By.ID, "main-content"))
    )


@then('The title of the method summary page is "{title}"')
def check_method_summary_title(context, title):
    page_title = (
        WebDriverWait(driver, timeout=timeout)
        .until(lambda d: d.find_element(By.TAG_NAME, "h1"))
        .text
    )
    assert page_title == title


# This test will check if the github resources are present.
# If they cannot be found the test will fail with a timeout error so asserts are not needed here.
@then("The {method_name} method has the expected github resources")
def check_method_has_github_resources(context, method_name):
    method_name = method_name.strip('"')

    method_spec_link_text = f"Go to {method_name} specification on GitHub"
    code_link_text = f"Go to {method_name} code on GitHub"
    user_docs_link_text = f"Go to {method_name} user documentation on GitHub"

    WebDriverWait(driver, timeout=timeout).until(
        lambda d: d.find_element(By.PARTIAL_LINK_TEXT, value=method_spec_link_text)
    )

    WebDriverWait(driver, timeout=timeout).until(
        lambda d: d.find_element(By.PARTIAL_LINK_TEXT, value=user_docs_link_text)
    )

    code_link = (
        WebDriverWait(driver, timeout=timeout)
        .until(lambda d: d.find_element(By.PARTIAL_LINK_TEXT, value=code_link_text))
        .get_attribute("href")
    )

    assert code_link.endswith(".py")


@then("The {metaDataField} of the method is {metaDataValue}")
def check_ons_meta_data(context, metaDataField, metaDataValue):
    ons_meta_data_fields = extract_ons_meta_data(context)[0]
    ons_meta_data_values = extract_ons_meta_data(context)[1]

    ons_meta_data_values = [
        val.replace("Release version\n", "").replace("\n(opens in a new tab)", "")
        for val in ons_meta_data_values
    ]

    metaDataField = metaDataField.strip('"')
    metaDataValue = metaDataValue.strip('"')

    check_duplicates = list(set(ons_meta_data_values))

    if metaDataField in ons_meta_data_fields and metaDataValue in ons_meta_data_values:
        if ons_meta_data_fields.index(metaDataField) == ons_meta_data_values.index(
            metaDataValue
        ) or len(ons_meta_data_values) != len(check_duplicates):
            assert True
        else:
            assert False
    else:
        assert False


def extract_ons_meta_data(context):
    main_content = WebDriverWait(driver, timeout=timeout).until(
        lambda d: d.find_element(By.ID, value="main-content")
    )
    ons_meta_data = main_content.find_element(By.TAG_NAME, "dl")
    ons_meta_data_fields = ons_meta_data.find_elements(By.TAG_NAME, "dt")
    ons_meta_data_values = ons_meta_data.find_elements(By.TAG_NAME, "dd")

    fields = []
    values = []

    for field in ons_meta_data_fields:
        fields.append(field.text)

    for value in ons_meta_data_values:
        values.append(value.text)

    return fields, values
