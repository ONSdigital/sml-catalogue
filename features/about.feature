# Tests for about page.

Feature: About library tests

    Scenario: Title check
        Given I'm an sml portal user
        When I navigate to the "about" page
        Then The id of the title is "about-page-content"
