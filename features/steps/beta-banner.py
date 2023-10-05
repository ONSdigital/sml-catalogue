# Tests for the beta banner in the preheader
# pylint: disable=import-error, undefined-variable, unused-argument, function-redefined

from setupSelenium import By, WebDriverWait, driver, timeout


@then('The banner mailto address is "{address}"')
def check_title(context, address):
    feedback_address = (
        WebDriverWait(driver, timeout=timeout)
        .until(lambda d: d.find_element(By.LINK_TEXT, "give feedback"))
        .get_attribute("href")
    )
    assert feedback_address == address
