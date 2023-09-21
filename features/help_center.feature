# Tests for help center page.

Feature: Help center tests

    Scenario: Title check
        Given I'm an sml portal user trying to get to the help centre
        When I navigate to the help centre page
        Then The title of the page is "Help centre"

    Scenario: Content check for external user
        Given I'm an sml portal user on the "submit a method request" page
        When I click the external user dropdown
        Then The drop down content is "Currently we do not accept formal method submissions or change requests from external users. In future, we will accept certain method requests via the Integrated Data Service https://integrateddataservice.gov.uk/. If you would like to make a suggestion for a new method, or to provide feedback about an existing method, please do so by emailing smlhelp@ons.gov.uk"

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

    Scenario: PEP8 link check for coding standards
        Given I'm an sml portal user on the "coding standards" page
        When I click the "PEP8" link
        Then The title of the page is "Python Enhancement Proposals"

    Scenario: GDS link check for coding standards
        Given I'm an sml portal user on the "coding standards" page
        When I click the "GDS" link
        Then The title of the page is "Python style guide"

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

    Scenario: Back link check for sub categories
        Given I'm an sml portal user on the "find and view methods" page
        When I click the "back" link
        Then The title of the page is "Help centre"

    Scenario: Back link check for submit a method request (uses different code to above test)
        Given I'm an sml portal user on the "submit a method request" page
        When I click the "back" link
        Then The title of the page is "Help centre"
