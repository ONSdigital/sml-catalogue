# Tests for winsorisation page.

Feature: Winsorisation tests

    Scenario: Title check
        Given I'm an sml portal user trying to get to the winsorisation method
        When I navigate to the winsorisation page
        Then The title of the winsorisation page is "Method: Winsorisation"