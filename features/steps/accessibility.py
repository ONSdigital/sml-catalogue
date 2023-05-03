# Tests for the accessibility preferences

from urllib.parse import urljoin
from setupSelenium import *

@then('The accessibility test passes')
def accessibility_check(context):
    driver.current_url
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


@when('I navigate to the help centre "{page}" page')
def navigate_to_page(context, page):
    path = ""
    if page == "submit a method request": path = "information/methods-request"
    if page == "how the methods are versioned": path = "information/version-methods"
    if page == "coding standards": path = "information/coding-standards"
    if page == "find and view methods": path = "access/view-methods"
    if page == "use a method": path = "access/run-a-method"
    if page == "report a defect or bug": path = "feedback/report-bug"
    if page == "provide feedback": path = "feedback/provide-feedback"
    if page == "get support": path = "support/support"
    if page == "get information on expert groups": path = "support/expert-groups"
    if page == "troubleshooting": path = "support/troubleshooting"
    if page == "using github": path = "support/github"
    driver.get(urljoin(context.config.userdata.get("host") + "help-centre/", path))
    WebDriverWait(driver, timeout=timeout).until(EC.presence_of_element_located((By.ID, 'main-content')))
