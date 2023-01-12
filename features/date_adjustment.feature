# Tests for date adjustment page.

Feature: Date adjustment tests

    Scenario: Title check
        Given I'm an sml portal user trying to get to the date adjustment method
        When I navigate to the date adjustment page
        Then The title of the date adjustment page is "Method: Date adjustment"