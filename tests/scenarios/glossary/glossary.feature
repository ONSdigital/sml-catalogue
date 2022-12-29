# Tests for glossary page.

Feature: Glossary tests

    Scenario: Title check
        Given I'm an sml portal user
        When I navigate to the glossary page
        Then The title of the page is "Library glossary"