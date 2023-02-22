# Step definitions for methods catalogue page

from setupSelenium import *

@given('I\'m an sml portal user on the home page')
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

@when('I click the "{page}" link in the header')
def navigate_to_url(context, page):
    if page == "methods catalogue":
        main_navigation =  WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.ID, value='main-navigation'))
        main_navigation.find_element(By.LINK_TEXT, value='Methods catalogue').click()
        WebDriverWait(driver, timeout=timeout).until(EC.presence_of_element_located((By.ID, 'collapsible')))
    elif page == "help centre":
        main_navigation =  WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.ID, value='main-navigation'))
        main_navigation.find_element(By.LINK_TEXT, value='Help centre').click()
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, 'main-content')))
    elif page == "about this library":
        main_navigation =  WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, value='main-navigation'))
        main_navigation.find_element(By.LINK_TEXT, value='About this library').click()
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, 'main-content')))
    elif page == "glossary":
        main_navigation =  WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, value='main-navigation'))
        main_navigation.find_element(By.LINK_TEXT, value='Glossary').click()
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, 'main-content')))

@then('The title of this page is "{title}"')
def check_title(context, title):
    page_title =  WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == title
