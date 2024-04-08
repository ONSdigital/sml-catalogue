# Tests for the search tool page.

Feature: Search tool tests

    Scenario: Partial search for method
        Given I am on the methods catalogue page
        When Search is active
        And I search for "Totals And"
        Then I see the the search results

    Scenario: Full search for method
        Given I am on the methods catalogue page
        When Search is active
        And I search for "Date Adjustment"
        Then I see the the search results

    Scenario: Invalid search
        Given I am on the methods catalogue page
        When Search is active
        And I search for ""
        Then I get an error message

    Scenario: No results search
        Given I am on the methods catalogue page
        When Search is active
        And I search for "Capri"
        Then I get no search results

    Scenario: Search is disabled
        Given I am on the methods catalogue page
        When Search is inactive
        Then I cannot perform a search