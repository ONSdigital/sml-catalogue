# Tests for accessibility page.

Feature: About library tests

    Scenario: Help centre page install a method accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre page
        Then The verified id for the page is "help-centre-content"
        And The accessibility test passes

    Scenario: Main accessibility check
        Given I'm an sml portal user
        When The page loads
        Then The accessibility test passes

    Scenario: Accessibility page accessibility check
        Given I'm an sml portal user
        When I navigate to "accessibility-statement"
        Then The verified id for the page is "accessibility-statement-content"
        And The accessibility test passes

    Scenario: Methods catalogue page accessibility check
        Given I'm an sml portal user
        When I navigate to the methods catalogue page
        Then The verified id for the page is "methods-catalogue-page-content"
        And The accessibility test passes

    Scenario: Glossary page accessibility check
        Given I'm an sml portal user on the home page
        When I click the "glossary" link in the header
        Then The verified id for the page is "glossary-page-content"
        And The accessibility test passes    
        
    Scenario: Cell Key Perturbation page accessibility check
    Given I'm an sml portal user
    When I navigate to the "Cell Key Perturbation" summary page
    Then The title of the page is "Method: Cell Key Perturbation"
    And The accessibility test passes

    Scenario: Totals and components page accessibility check
        Given I'm an sml portal user
        When I navigate to the "Totals and Components" summary page
        Then The title of the page is "Method: Totals and Components"
        And The accessibility test passes

    Scenario: Date Adjustment summary page accessibility check
        Given I'm an sml portal user
        When I navigate to the "Date Adjustment" summary page
        Then The title of the page is "Method: Date Adjustment"
        And The accessibility test passes

    Scenario: Selective Editing summary page accessibility check
        Given I'm an sml portal user
        When I navigate to the "Selective Editing" summary page
        Then The title of the page is "Method: Selective Editing"
        And The accessibility test passes

    Scenario: Thousand Pound Estimation summary page accessibility check
        Given I'm an sml portal user
        When I navigate to the "Thousand Pound Correction" summary page
        Then The title of the page is "Method: Thousand Pound Correction"
        And The accessibility test passes