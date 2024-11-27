# Tests for Methods catalogue page.

Feature: Methods catalogue tests

    Scenario: Title check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The verified id for the page is "methods-catalogue-page-content"

    Scenario: Check for dropdown content
        Given I am on the methods catalogue page
        When I click on the collapsible drop down
        Then The id of the dropdown is "collapsible-content"

    Scenario: Methods catalogue ready table header check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The "ready" table headings of the methods catalogue table are "Name" "Theme" "Expert group" "Languages"

    Scenario: Methods catalogue future table header check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The "future" table headings of the methods catalogue table are "Name" "Theme" "Expert group" "Languages"

    Scenario: Cell Key Perturbation R table row check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The "future" table row of the method are "Cell Key Perturbation" "Statistical Disclosure Control" "Statistical Disclosure Control" "R"

    Scenario: Cell Key Perturbation Python table row check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The "ready" table row of the method are "Cell Key Perturbation" "Statistical Disclosure Control" "Statistical Disclosure Control" "Python"

    Scenario: Totals and Components table row check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The "ready" table row of the method are "Totals and Components" "Editing" "Editing & Imputation" "Python"

    Scenario: Date adjustment table row check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The "ready" table row of the method are "Date Adjustment" "Editing" "Editing & Imputation" "Python"
    
    Scenario: Selective editing table row check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The "ready" table row of the method are "Selective Editing" "Editing" "Editing & Imputation" "Python"

    Scenario: Thousand pound correction table row check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The "ready" table row of the method are "Thousand Pound Correction" "Editing" "Editing & Imputation" "Python"
