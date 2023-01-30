# Tests for HT/Ratio estimation page.

Feature: HT/Ratio estimation tests

    Scenario: Title check
        Given I'm an sml portal user trying to get to the ht/ratio estimation method
        When I navigate to the ht/ratio estimation page
        Then The title of the ht/ratio estimation page is "Method: Horvitz-Thompson Ratio Estimator"