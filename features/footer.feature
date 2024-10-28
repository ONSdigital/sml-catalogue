# Footer feature tests

Feature: Footer pages tests

    Scenario: Accessibility statement page check
        Given I'm an sml portal user trying to get to the "accessibility statement" page
        When I click the "Accessibility Statement" page on the footer
        Then The verified id is "accessibility-statement-content"
    
    Scenario: Cookies page check
        Given I'm an sml portal user trying to get to the "cookies" page
        When I click the "Cookies" page on the footer
        Then The verified id is "cookies-page-content"
    
    Scenario: Privacy and data protection page check
        Given I'm an sml portal user trying to get to the "privacy and data protection" page
        When I click the "Privacy and Data Protection" page on the footer
        Then The verified id is "privacy-and-data-protection-page-content"
