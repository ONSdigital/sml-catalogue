# Tests for the date adjustment link

from setupSelenium import *


@given('I\'m an sml portal user trying to get to the "{page}" page')
def auth_user(context, page):
    driver.get(host)
    axe = Axe(driver)
    # Inject axe-core javascript into page.
    axe.inject()
    # Run axe accessibility checks.
    results = axe.run()
    # Write results to file
    axe.write_results(results, 'axeResults.json')
    violations = results["violations"]
    violationCount = 0
    # Filter out minor and moderate error alerts
    for i in range(len(violations)):
        if violations[i]["impact"] in ('critical', 'serious'):
            violationCount += 1
    # Assert no violations are found
    assert violationCount == 0


@when('I click the "{page}" page on the footer')
def navigate_to_url(context, page):
    WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.LINK_TEXT, value=page)).click()
    WebDriverWait(driver, timeout=timeout).until(EC.presence_of_element_located((By.ID, 'main-content')))


@then('The title of page is "{title}"')
def check_title(context, title):
    page_title = WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == title
