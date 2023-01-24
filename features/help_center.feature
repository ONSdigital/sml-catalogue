# Tests for help center page.

Feature: Help center tests

    Scenario: Title check
        Given I'm an sml portal user trying to get to the help centre
        When I navigate to the help centre page
        Then The title of the help centre page is "Help centre"
    
    Scenario: Content check for external user
        Given I am on the how to submit a method request page
        When I click the external user dropdown
        Then The drop down content is "Currently we do not accept formal method submissions or change requests from external users. In future, we will accept certain method requests via the Integrated Data Service https://integrateddataservice.gov.uk/. If you would like to make a suggestion for a new method, or to provide feedback about an existing method, please do so by emailing smlhelp@ons.gov.uk"