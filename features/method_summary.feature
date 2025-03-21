# Tests for method summary page.

Feature: Method summary page tests

    Scenario: Date adjustment check
        Given I'm an sml portal user trying to get to the "date adjustment method" summary page
        When I navigate to the "Date Adjustment" summary page
        Then The title of the method summary page is "Method: Date Adjustment"
        And The "Author" of the method is "ONS"
        And The "Theme" of the method is "Editing"
        And The "Expert group" of the method is "Editing & Imputation"
        And The "Languages" of the method is "Python"
        And The "Release" of the method is "v1.2.4"
        And The "Date Adjustment" method has the expected github resources

    Scenario: Thousand pound correction check
        Given I'm an sml portal user trying to get to the "thousand pound correction method" summary page
        When I navigate to the "Thousand Pound Correction" summary page
        Then The title of the method summary page is "Method: Thousand Pound Correction"
        And The "Author" of the method is "ONS"
        And The "Theme" of the method is "Editing"
        And The "Expert group" of the method is "Editing & Imputation"
        And The "Languages" of the method is "Python"
        And The "Release" of the method is "v1.2.4"
        And The "Thousand Pound Correction" method has the expected github resources

    Scenario: Selective editing check
        Given I'm an sml portal user trying to get to the "selective editing method" summary page
        When I navigate to the "Selective Editing" summary page
        Then The title of the method summary page is "Method: Selective Editing"
        And The "Author" of the method is "ONS"
        And The "Theme" of the method is "Editing"
        And The "Expert group" of the method is "Editing & Imputation"
        And The "Languages" of the method is "Python"
        And The "Release" of the method is "v1.2.4"
        And The "Selective Editing" method has the expected github resources

    Scenario: Cell Key Perturbation check
        Given I'm an sml portal user trying to get to the "cell key perturbation method" summary page
        When I navigate to the "Cell Key Perturbation" summary page
        Then The title of the method summary page is "Method: Cell Key Perturbation"
        And The "Author" of the method is "ONS"
        And The "Theme" of the method is "Statistical Disclosure Control"
        And The "Expert group" of the method is "Statistical Disclosure Control"
        And The "Languages" of the method is "Python"
        And The "Release" of the method is "v2.0.0"
    
    Scenario: Totals and Components check
        Given I'm an sml portal user trying to get to the "totals and components method" summary page
        When I navigate to the "Totals and Components" summary page
        Then The title of the method summary page is "Method: Totals and Components"
        And The "Author" of the method is "ONS"
        And The "Theme" of the method is "Editing"
        And The "Expert group" of the method is "Editing & Imputation"
        And The "Languages" of the method is "Python"
        And The "Release" of the method is "v1.2.4"
        And The "Totals and Components" method has the expected github resources
        
