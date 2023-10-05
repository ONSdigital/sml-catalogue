# Tests for beta banner.

Feature: Beta banner

    Scenario: Beta banner feedback link check
        Given I'm an sml portal user
        Then The banner mailto address is "mailto:smlhelp@ons.gov.uk"