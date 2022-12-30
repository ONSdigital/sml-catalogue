# Tests for all methods page.

Feature: Methods catalogue tests

    Scenario: Title check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The title of the methods catalogue page is "All methods"