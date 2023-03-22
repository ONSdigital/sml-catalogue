# Tests for method summary page.

Feature: Method summary page tests

    Scenario: Date adjustment check
        Given I'm an sml portal user trying to get to the "date adjustment method" summary page
        When I navigate to the "Date Adjustment" summary page
        Then The title of the method summary page is "Method: Date Adjustment"
        And The "Author" of the method is "ONS"
        And The "Theme" of the method is "Editing"
        And The "Expert group" of the method is "Editing & Imputation"
        And The "Languages" of the method is "Python/Pandas"
        And The "Release" of the method is "v1.0.0"

    Scenario: Horvitz-thompson ratio estimator check
        Given I'm an sml portal user trying to get to the "ht/ratio estimation method" summary page
        When I navigate to the "Horvitz-Thompson Ratio Estimator" summary page
        Then The title of the method summary page is "Method: Horvitz-Thompson Ratio Estimator"
        And The "Author" of the method is "ONS"
        And The "Theme" of the method is "Sample Design & Estimation"
        And The "Expert group" of the method is "Sample Design & Estimation"
        And The "Languages" of the method is "Python/PySpark"
        And The "Release" of the method is "Not Released Yet"

    Scenario: Ratio of means check
        Given I'm an sml portal user trying to get to the "ratio of means method" summary page
        When I navigate to the "Ratio of Means" summary page
        Then The title of the method summary page is "Method: Ratio of Means"
        And The "Author" of the method is "ONS"
        And The "Theme" of the method is "Imputation"
        And The "Expert group" of the method is "Editing & Imputation"
        And The "Languages" of the method is "Python/PySpark"
        And The "Release" of the method is "Not Released Yet"

    Scenario: Selective editing check
        Given I'm an sml portal user trying to get to the "selective editing method" summary page
        When I navigate to the "Selective Editing" summary page
        Then The title of the method summary page is "Method: Selective Editing"
        And The "Author" of the method is "ONS"
        And The "Theme" of the method is "Editing"
        And The "Expert group" of the method is "Editing & Imputation"
        And The "Languages" of the method is "Python/Pandas"
        And The "Release" of the method is "v1.0.0"

    Scenario: Thousand pound correction check
        Given I'm an sml portal user trying to get to the "thousand pound correction method" summary page
        When I navigate to the "Thousand Pound Correction" summary page
        Then The title of the method summary page is "Method: Thousand Pound Correction"
        And The "Author" of the method is "ONS"
        And The "Theme" of the method is "Editing"
        And The "Expert group" of the method is "Editing & Imputation"
        And The "Languages" of the method is "Python/Pandas"
        And The "Release" of the method is "Not Released Yet"

    Scenario: Winsorisation check
        Given I'm an sml portal user trying to get to the "winsorisation method" summary page
        When I navigate to the "Winsorisation" summary page
        Then The title of the method summary page is "Method: Winsorisation"
        And The "Author" of the method is "ONS"
        And The "Theme" of the method is "Sample Design & Estimation"
        And The "Expert group" of the method is "Sample Design & Estimation"
        And The "Languages" of the method is "Python/PySpark"
        And The "Release" of the method is "Not Released Yet"

    Scenario: General Linear Model (GLM) check
        Given I'm an sml portal user trying to get to the "General Linear Model (GLM) method" summary page
        When I navigate to the "General Linear Model (GLM)" summary page
        Then The title of the method summary page is "Method: General Linear Model (GLM)"
        And The "Author" of the method is "R Core Team"
        And The "Theme" of the method is "Regression"
        And The "Expert group" of the method is "Analysis"
