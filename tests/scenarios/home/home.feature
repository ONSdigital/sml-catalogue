# all the scenario tests for the home page of the portal. These cover link/button clicks.

Feature: Blog
    A site where you can publish your articles.

    Scenario: Publishing the article
        Given I'm an author user
        And I have an article
