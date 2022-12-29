# content of home page.

Feature: Home page tests

    Scenario: Refresh page and title check
        Given I'm an sml portal user
        When I refresh the page
        Then The page will load
        And The title of the page is Discover methods used by the Office for National Statistics

    Scenario: Check about link works
        Given I'm an sml portal user
        When I click the about library link
        Then I should be taken to the about library page

    Scenario: Check methods catalogue link works
        Given I'm an sml portal user
        When I click the methods catalogue library link
        Then I should be taken to the methods catalogue page

    Scenario: Check methods catalogue header link works
        Given I'm an sml portal user
        When I click the methods catalogue library header link
        Then I should be taken to the methods catalogue page

    Scenario: Check methods catalogue button works
        Given I'm an sml portal user
        When I click the find methods button
        Then I should be taken to the methods catalogue page

    Scenario: Check help center link works
        Given I'm an sml portal user
        When I click the help center link
        Then I should be taken to the help center page

    Scenario: Check help center header link works
        Given I'm an sml portal user
        When I click the help center header link
        Then I should be taken to the help center page

    Scenario: Check glossary link works
        Given I'm an sml portal user
        When I click the glossary link
        Then I should be taken to the glossary page
