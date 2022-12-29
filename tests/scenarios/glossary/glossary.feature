# Tests for glossary page.

Feature: Glossary tests

    Scenario: Title check
        Given I'm an sml portal user
        When I am on the glossary page
        Then The title of the page is "Library glossary"