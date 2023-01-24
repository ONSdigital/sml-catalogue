# Tests for help center page.

Feature: Help center tests

    Scenario: Title check
        Given I'm an sml portal user trying to get to the help centre
        When I navigate to the help centre page
        Then The title of the help centre page is "Help centre"

    Scenario: Sub-title check for find and view methods
        Given I'm an sml portal user trying to get to the help centre
        When I navigate to the help centre page
        Then The subtitle of the help centre page is "Find and view methods"

    Scenario: Sub-title check for submit a method request
        Given I'm an sml portal user trying to get to the help centre
        When I navigate to the help centre page
        Then The subtitle of the help centre page is "Submit a method request"

    Scenario: Sub-title check for how the methods are versioned
        Given I'm an sml portal user trying to get to the help centre
        When I navigate to the help centre page
        Then The subtitle of the help centre page is "How the methods are versioned"

    Scenario: Sub-title check for coding standards
        Given I'm an sml portal user trying to get to the help centre
        When I navigate to the help centre page
        Then The subtitle of the help centre page is "Coding standards"

    Scenario: Sub-title check for use a method
        Given I'm an sml portal user trying to get to the help centre
        When I navigate to the help centre page
        Then The subtitle of the help centre page is "Use a method"

    Scenario: Sub-title check for report a defect or bug
        Given I'm an sml portal user trying to get to the help centre
        When I navigate to the help centre page
        Then The subtitle of the help centre page is "Report a defect or bug"

    Scenario: Sub-title check for provide feedback
        Given I'm an sml portal user trying to get to the help centre
        When I navigate to the help centre page
        Then The subtitle of the help centre page is "Provide feedback"

    Scenario: Sub-title check for get support
        Given I'm an sml portal user trying to get to the help centre
        When I navigate to the help centre page
        Then The subtitle of the help centre page is "Get support"

    Scenario: Sub-title check for get information on expert groups
        Given I'm an sml portal user trying to get to the help centre
        When I navigate to the help centre page
        Then The subtitle of the help centre page is "Get information on expert groups"

    Scenario: Sub-title check for troubleshooting
        Given I'm an sml portal user trying to get to the help centre
        When I navigate to the help centre page
        Then The subtitle of the help centre page is "Troubleshooting"

    Scenario: Sub-title check for using github
        Given I'm an sml portal user trying to get to the help centre
        When I navigate to the help centre page
        Then The subtitle of the help centre page is "Using GitHub"
