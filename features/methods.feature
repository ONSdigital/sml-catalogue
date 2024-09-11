# Tests for Methods catalogue page.

Feature: Methods catalogue tests

    Scenario: Title check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The title of the methods catalogue page is "Methods catalogue"

    Scenario: Check for dropdown content
        Given I am on the methods catalogue page
        When I click on the collapsible drop down
        Then I see the dropdown content "Methods are sorted in hierarchical order with expert groups as the top level. For example, within an expert group are different themes, and within the themes are different methods.To find out more about expert groups and themes, please visit the analysis function website."

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
        Then The "ready" table row of the method are "Cell Key Perturbation" "Statistical Disclosure Control" "Statistical Disclosure Control" "Python/Pandas"

    Scenario: Totals and Components table row check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The "ready" table row of the method are "Totals and Components" "Editing" "Editing & Imputation" "Python/Pandas"

    Scenario: Date adjustment table row check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The "ready" table row of the method are "Date Adjustment" "Editing" "Editing & Imputation" "Python/Pandas"
    
    Scenario: Selective editing table row check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The "ready" table row of the method are "Selective Editing" "Editing" "Editing & Imputation" "Python/Pandas"

    Scenario: Thousand pound correction table row check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The "ready" table row of the method are "Thousand Pound Correction" "Editing" "Editing & Imputation" "Python/Pandas"
