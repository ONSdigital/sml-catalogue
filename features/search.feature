# # Tests for the search tool page.

# Feature: Search tool tests

#     Scenario: Partial search for method
#         Given I am on the methods catalogue page
#         When Search is active
#         And I search for "Totals And"
#         Then I see the the search results for "Totals And"

#     Scenario: Full search for method
#         Given I am on the methods catalogue page
#         When Search is active
#         And I search for "Date Adjustment"
#         Then I see the the search results for "Date Adjustment"

#     Scenario: Invalid search
#         Given I am on the methods catalogue page
#         When Search is active
#         And I search for ""
#         Then I get an error message

#     Scenario: No results search
#         Given I am on the methods catalogue page
#         When Search is active
#         And I search for "Capri"
#         Then I get no search results

#     Scenario: Clear search
#         Given I am on the methods catalogue page
#         When Search is active
#         And I search for "Date Adjustment"
#         And I see the the search results for "Date Adjustment"
#         And I click the clear button
#         Then The page is reset