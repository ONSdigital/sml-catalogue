# Step definitions for about page
from urllib.parse import urljoin
from setupSelenium import * 


@given('I\'m an sml portal user')
def auth_user(context):
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
    page_title = WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == 'An open source library for statistical code approved by the ONS'


@when('I navigate to the "{page}" page')
def navigate_to_url(context, page):
    driver.get(urljoin(host + "resources/", page))
    WebDriverWait(driver, timeout=timeout).until(EC.presence_of_element_located((By.ID, 'main-content')))


@then('The title of the page is "{title}"')
def check_title(context, title):
    page_title = WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == title

@then('The subtitle of the page is "{subtitle}"')
def check_subtitle(context, subtitle):
    page_subtitle = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, "page-subtitle")).text
    assert page_subtitle == subtitle