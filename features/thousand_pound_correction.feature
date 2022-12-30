# Tests for thousand pound correction page.

Feature: Thousand pound correction tests

    Scenario: Title check
        Given I'm an sml portal user trying to get to the thousand pound correction method
        When I navigate to the thousand pound correction page
        Then The title of the thousand pound correction page is "Method: Thousand pound correction"