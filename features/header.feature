# content of home page.

Feature: Home page tests
    Scenario: Check methods catalogue header link works
        Given I'm an sml portal user on the home page
        When I click the "methods catalogue" link in the header
        Then The title of this page is "Methods catalogue"

    Scenario: Check help centre header link works
        Given I'm an sml portal user on the home page
        When I click the "help centre" link in the header
        Then The title of this page is "Help centre"