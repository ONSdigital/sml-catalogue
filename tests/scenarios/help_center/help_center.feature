# Tests for help center page.

Feature: Help center tests

    Scenario: Title check
        Given I'm an sml portal user
        When I navigate to the help center page
        Then The title of the page is ""Help center""