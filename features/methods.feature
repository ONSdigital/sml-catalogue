# Tests for Methods catalogue page.

Feature: Methods catalogue tests

    Scenario: Title check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The title of the methods catalogue page is "Methods catalogue"

    Scenario: Check for dropdown content
        Given I am on the methods catalogue page
        When I click on the collapsible drop down
        Then I see the dropdown content "Methods are sorted in hierarchical order with expert groups as the top level. For example, within an expert group are different themes, and within the themes are different methods. To find out more about expert groups and themes, please visit the analysis function website."

    Scenario: Methods catalgoue table header check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The table headings of the methods catalogue table are "Name" "Theme" "Expert group" "Languages" "Status"

    Scenario: Ratio of Means table row check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The table row of the method are "Ratio of Means" "Imputation" "Editing & Imputation" "Python/PySpark" "In development"

    Scenario: Winsorisation table row check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The table row of the method are "Winsorisation" "Sample Design & Estimation" "Sample Design & Estimation" "Python/PySpark" "In development"

    Scenario: Thousand pound correction table row check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The table row of the method are "Thousand Pound Correction" "Editing" "Editing & Imputation" "Python/Pandas" "Approved for development"

    Scenario: Horvitz-Thompson Ratio Estimator table row check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The table row of the method are "Horvitz-Thompson Ratio Estimator" "Sample Design & Estimation" "Sample Design & Estimation" "Python/PySpark" "In development"
    
    Scenario: Date adjustment table row check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The table row of the method are "Date Adjustment" "Editing" "Editing & Imputation" "Python/Pandas" "Complete"
    
    Scenario: Selective editing table row check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The table row of the method are "Selective Editing" "Editing" "Editing & Imputation" "Python/Pandas" "Complete"
