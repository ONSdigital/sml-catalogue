# Tests for glossary page.

Feature: Glossary tests

    Scenario: Title check
        Given I'm an sml portal user
        When I navigate to the "glossary" page
        Then The title of the page is "Library glossary"

    Scenario: Subtitle check
        Given I'm an sml portal user
        When I navigate to the "glossary" page
        Then The subtitle of the page is "Definitions of words, phrases, and abbreviations used within the Statistical Methods Library"
