# content of home page.

Feature: Home page tests
    Scenario: Check methods catalogue header link works
        Given I'm an sml portal user on the home page
        When I click the "methods catalogue" link in the header
        Then The verified id is "methods-catalogue-page-content"

    Scenario: Check help centre header link works
        Given I'm an sml portal user on the home page
        When I click the "help centre" link in the header
        Then The verified id is "help-centre-content"

    Scenario: Check about this library header link works
        Given I'm an sml portal user on the home page
        When I click the "about this library" link in the header
        Then The verified id is "about-page-content"

    Scenario: Check glossary header link works
        Given I'm an sml portal user on the home page
        When I click the "glossary" link in the header
        Then The verified id is "glossary-page-content"
        
    Scenario: Beta banner feedback link check
        Given I'm an sml portal user
        When I click the "home" link in the header
        Then The banner mailto address is "mailto:smlhelp@ons.gov.uk"
