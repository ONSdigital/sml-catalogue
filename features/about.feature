# Tests for about page.

Feature: About library tests

    Scenario: Title check
        Given I'm an sml portal user
        When I navigate to the "about" page
        Then The title of the page is "About the Statistical Methods Library"
