# Tests for about page.

Feature: About library tests

    Scenario: Title check
        Given I'm an sml portal user on the home page
        When I click the "about this library" link in the header
        Then The verified id for the page is "about-page-content"
