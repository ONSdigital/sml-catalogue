# Tests for date adjustment page.

Feature: Date adjustment tests

    Scenario: Title check
        Given I'm an sml portal user
        When I navigate to the date adjustment page
        Then The title of the page is "Method: Date adjustment"