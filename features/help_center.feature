# Tests for help center page.

Feature: Help center tests

    Scenario: Title check
        Given I'm an sml portal user trying to get to the help centre
        When I navigate to the help centre page
        Then The verified id for the page is "help-centre-content"
