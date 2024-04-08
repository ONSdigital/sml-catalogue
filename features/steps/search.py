# Step definitions for methods catalogue page search tool
# pylint: disable=import-error, undefined-variable, unused-argument, function-redefined

from setupSelenium import EC, By, WebDriverWait, driver, timeout
from sml_builder.utils import get_feature_config


@when("Search is active")
def auth_user(context):
    content_management = get_feature_config("content_management")
    

@when("Search is inactive")
def auth_user(context):
    driver.get(context.config.userdata.get("host"))