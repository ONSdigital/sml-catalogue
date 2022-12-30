# Tests for HT/Ratio estimation page.

Feature: HT/Ratio estimation tests

    Scenario: Title check
        Given I'm an sml portal user
        When I navigate to the ht/ratio estimation page
        Then The title of the page is "Method: HT/Ratio Estimation"