# Tests for method summary page.

Feature: Method summary page tests

    Scenario: Date adjustment check
        Given I'm an sml portal user trying to get to the "date adjustment method" summary page
        When I navigate to the "Date Adjustment" summary page
        Then The title of the method summary page is "Method: Date Adjustment"
        And The "Author" of the method is "ONS"
        And The "Theme" of the method is "Editing"
        And The "Expert group" of the method is "Editing & Imputation"
        And The "Langauges" of the method is "Python/Pandas"
        And The "Release" of the method is "v1.0.0"

    Scenario: Horvitz-thompson ratio estimator check
        Given I'm an sml portal user trying to get to the "ht/ratio estimation method" summary page
        When I navigate to the "Horvitz-Thompson Ratio Estimator" summary page
        Then The title of the method summary page is "Method: Horvitz-Thompson Ratio Estimator"

    Scenario: Ratio of means check
        Given I'm an sml portal user trying to get to the "ratio of means method" summary page
        When I navigate to the "Ratio of Means" summary page
        Then The title of the method summary page is "Method: Ratio of Means"

    Scenario: Selective editing check
        Given I'm an sml portal user trying to get to the "selective editing method" summary page
        When I navigate to the "Selective Editing" summary page
        Then The title of the method summary page is "Method: Selective Editing"

    Scenario: Thousand pound correction check
        Given I'm an sml portal user trying to get to the "thousand pound correction method" summary page
        When I navigate to the "Thousand Pound Correction" summary page
        Then The title of the method summary page is "Method: Thousand Pound Correction"

    Scenario: Winsorisation check
        Given I'm an sml portal user trying to get to the "winsorisation method" summary page
        When I navigate to the "Winsorisation" summary page
        Then The title of the method summary page is "Method: Winsorisation"
