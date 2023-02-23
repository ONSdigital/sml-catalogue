# Tests for abaccessibilityout page.

Feature: About library tests

    Scenario:Home page accessibility check
        Given I'm an sml portal user
        When I refresh the page
        Then The accessibility test passes

    Scenario: Help centre page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "submit a method request" page
        Then The accessibility test passes

    Scenario: Submit a method request page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "how the methods are versioned" page
        Then The accessibility test passes

    Scenario: Help centre page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "coding standards" page
        Then The accessibility test passes

    Scenario: Help centre page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "find and view methods" page
        Then The accessibility test passes

    Scenario: Help centre page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "use a method" page
        Then The accessibility test passes

    Scenario: Help centre page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "report a defect or bug" page
        Then The accessibility test passes

    Scenario: Help centre page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "provide feedback" page
        Then The accessibility test passes

    Scenario: Help centre page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "get support" page
        Then The accessibility test passes

    Scenario: Help centre page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "get information on expert groups" page
        Then The accessibility test passes

    Scenario: Help centre page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "troubleshooting" page
        Then The accessibility test passes

    Scenario: Help centre page accessibility check
        Given I'm an sml portal user
        When I navigate to the help centre "using github" page
        Then The accessibility test passes

    Scenario: Accessibility page accessibility check
        Given I'm an sml portal user
        When I navigate to "accessibility-statement"
        Then The accessibility test passes

    Scenario: Methods catalogue page accessibility check
        Given I'm an sml portal user
        When I navigate to "methods"
        Then The accessibility test passes

    Scenario: Glossary page accessibility check
        Given I'm an sml portal user
        When I navigate to the "glossary" page
        Then The accessibility test passes

    Scenario: Winsorisation page accessibility check
        Given I'm an sml portal user
        When I navigate to the "Winsorisation" summary page
        Then The accessibility test passes

    Scenario: Date Adjustment summary page accessibility check
        Given I'm an sml portal user
        When I navigate to the "Date Adjustment" summary page
        Then The accessibility test passes

    Scenario: Selective Editing summary page accessibility check
        Given I'm an sml portal user
        When I navigate to the "Selective Editing" summary page
        Then The accessibility test passes

    Scenario: Horvitz-Thompson Ratio Estimator summary page accessibility check
        Given I'm an sml portal user
        When I navigate to the "Horvitz-Thompson Ratio Estimator" summary page
        Then The accessibility test passes

    Scenario: Ratio of means summary page accessibility check
        Given I'm an sml portal user
        When I navigate to the "Ratio of Means" summary page
        Then The accessibility test passes

    Scenario: Thousand Pound Estimation summary page accessibility check
        Given I'm an sml portal user
        When I navigate to the "Thousand Pound Correction" summary page
        Then The accessibility test passes