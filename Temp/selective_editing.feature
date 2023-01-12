# Tests for selective editing page.

Feature: Selective editing tests

    Scenario: Title check
        Given I'm an sml portal user trying to get to the selective editing method
        When I navigate to the selective editing page
        Then The title of the selective editing page is "Method: Selective Editing"