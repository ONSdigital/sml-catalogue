# Tests for ratio of means page.

Feature: Ratio of means tests

    Scenario: Title check
        Given I'm an sml portal user trying to get to the ratio of means method
        When I navigate to the ratio of means page
        Then The title of the ratio of means page is "Method: Ratio of Means"