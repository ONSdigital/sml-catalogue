# Tests for the accessibility preferences
# pylint: disable=import-error, undefined-variable, unused-argument, function-redefined


from setupSelenium import Axe, driver


@then("The accessibility test passes")
def accessibility_check(context):
    axe = Axe(driver)
    # Inject axe-core javascript into page.
    axe.inject()
    # Run axe accessibility checks.
    results = axe.run()
    # Write results to file
    axe.write_results(results, "axeResults.json")
    violations = results["violations"]
    violationCount = 0
    # Filter out minor and moderate error alerts
    for violation in violations:
        if violation["impact"] in {"critical", "serious"}:
            violationCount += 1
    # Assert no violations are found
    assert violationCount == 0
