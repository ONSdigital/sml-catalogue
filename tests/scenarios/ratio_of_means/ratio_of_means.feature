# Tests for ratio of means page.

Feature: Ratio of means tests

    Scenario: Title check
        Given I'm an sml portal user
        When I am on the ratio of means page
        Then The title of the page is "Method: Ratio of Means"