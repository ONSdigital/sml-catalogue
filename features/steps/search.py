# # Step definitions for methods catalogue page search tool
# # pylint: disable=import-error, undefined-variable, unused-argument, function-redefined

# from setupSelenium import EC, By, WebDriverWait, driver, timeout
# from sml_builder.utils import update_feature_config
# from selenium.webdriver.common.keys import Keys

# @when("Search is active")
# def activate_search(context):
#     boolean = True
#     update_feature_config("method_search", boolean)
#     driver.refresh()

# @when("I search for {search_term}")
# def search_tables(context):
#     search_field = WebDriverWait(driver, timeout=timeout).until(
#         lambda d: d.find_element(By.ID, value="search-field")
#     ).send_keys("{search_term}")
#     # Press Enter to perform the search
#     search_field.send_keys(Keys.RETURN)
