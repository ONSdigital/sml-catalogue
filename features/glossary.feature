# Tests for glossary page.

Feature: Glossary tests

    Scenario: Title check
        Given I'm an sml portal user on the home page
        When I click the "glossary" link in the header
        Then The verified id for the page is "glossary-page-content"

    Scenario: Subtitle check
        Given I'm an sml portal user on the home page
        When I click the "glossary" link in the header
        Then The verified id for the page is "glossary-page-subtitle"
