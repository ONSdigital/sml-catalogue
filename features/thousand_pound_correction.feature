# Tests for Thousand pound correction page.

Feature: Thousand pound correction tests

    Scenario: Title check
        Given I'm an sml portal user
        When I navigate to the thousand pound correction page
        Then The title of the page is "Method: Thousand pound correction"