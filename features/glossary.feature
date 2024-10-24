# Tests for glossary page.

Feature: Glossary tests

    Scenario: Title check
        Given I'm an sml portal user
        When I navigate to the "glossary" page
        Then The id of the title is "glossary-page-content"

    Scenario: Subtitle check
        Given I'm an sml portal user
        When I navigate to the "glossary" page
        Then The id of the title is "glossary-page-subtitle"
