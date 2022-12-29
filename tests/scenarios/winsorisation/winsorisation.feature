# Tests for winsorisation page.

Feature: Winsorisation tests

    Scenario: Title check
        Given I'm an sml portal user
        When I am on the winsorisation page
        Then The title of the page is "Method: Winsorisation"