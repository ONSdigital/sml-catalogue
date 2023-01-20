# Tests for all methods page.

Feature: Methods catalogue tests

    Scenario: Title check
        Given I'm an sml portal user trying to get to the methods catalogue page
        When I navigate to the methods catalogue page
        Then The title of the methods catalogue page is "All methods"

    Scenario: Title check
        Given I am on the methods catalogue page
        When I click on the collapsible drop down
        Then I see the dropdown content "Method are sorted in hierarchical order with expert groups as the top level. For example, within an expert group are different themes, and within the themes are different methods. To find out more about expert groups and themes, please visit the analysis function website."