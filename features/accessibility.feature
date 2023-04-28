# Tests for abaccessibilityout page.

Feature: About library tests

    Scenario: Home page accessibility check
        Given I'm an sml portal user
        When I refresh the page
        Then The title of the page is "An open source library for statistical code approved by the ONS"
        And The accessibility test passes

    Scenario: Help centre page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "submit a method request" page
        Then The title of the help centre page is "Submit a method request"
        And The accessibility test passes

    Scenario: Submit a method request page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "how the methods are versioned" page
        Then The title of the help centre page is "How the methods are versioned"
        And The accessibility test passes

    Scenario: Help centre page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "coding standards" page
        Then The title of the help centre page is "Coding standards"
        And The accessibility test passes

    Scenario: Help centre page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "find and view methods" page
        Then The title of the help centre page is "Find and view methods"
        And The accessibility test passes

    Scenario: Help centre page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "use a method" page
        Then The title of the help centre page is "Use a method"
        And The accessibility test passes

    Scenario: Help centre page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "report a defect or bug" page
        Then The title of the help centre page is "Report a defect or bug"
        And The accessibility test passes

    Scenario: Help centre page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "provide feedback" page
        Then The title of the help centre page is "Provide feedback"
        And The accessibility test passes

    Scenario: Help centre page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "get support" page
        Then The title of the help centre page is "Get support"
        And The accessibility test passes

    Scenario: Help centre page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "get information on expert groups" page
        Then The title of the help centre page is "Get information on expert groups"
        And The accessibility test passes

    Scenario: Help centre page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "troubleshooting" page
        Then The title of the help centre page is "Troubleshooting"
        And The accessibility test passes

    Scenario: Help centre page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "using github" page
        Then The title of the help centre page is "Using GitHub"
        And The accessibility test passes

    Scenario: Accessibility page accessibility check
        Given I'm an sml portal user
        When I navigate to "accessibility-statement"
        Then The title of the page is "Accessibility statement"
        And The accessibility test passes

    Scenario: Methods catalogue page accessibility check
        Given I'm an sml portal user
        When I navigate to "methods"
        Then The title of the page is "Methods catalogue"
        And The accessibility test passes

    Scenario: Glossary page accessibility check
        Given I'm an sml portal user
        When I navigate to the "glossary" page
        Then The title of the page is "Library glossary"
        And The accessibility test passes

    Scenario: Winsorisation page accessibility check
        Given I'm an sml portal user
        When I navigate to the "Winsorisation" summary page
        Then The title of the page is "Method: Winsorisation"
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

    Scenario: Horvitz-Thompson Ratio Estimator summary page accessibility check
        Given I'm an sml portal user
        When I navigate to the "Horvitz-Thompson Ratio Estimator" summary page
        Then The title of the page is "Method: Horvitz-Thompson Ratio Estimator"
        And The accessibility test passes

    Scenario: Ratio of means summary page accessibility check
        Given I'm an sml portal user
        When I navigate to the "Ratio of Means" summary page
        Then The title of the page is "Method: Ratio of Means"
        And The accessibility test passes

    Scenario: Thousand Pound Estimation summary page accessibility check
        Given I'm an sml portal user
        When I navigate to the "Thousand Pound Correction" summary page
        Then The title of the page is "Method: Thousand Pound Correction"
        And The accessibility test passes