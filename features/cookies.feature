# content of home page.

Feature: Cookie banner tests
    Scenario: Accept cookies test
        Given I'm an sml portal user on the home page with a cookie banner
        When I click the accept cookies button in the header
        Then The cookie banner displays "You have accepted all additional cookies. You can change your cookie preferences at any time."

    # Scenario: Reject cookies test
    #     Given I'm an sml portal user on the home page with a cookie banner
    #     When I click the reject cookies button in the header
    #     Then The cookie banner displays "You have rejected all additional cookies. You can change your cookie preferences at any time."
    
    # Scenario: Additional cookies link test
    #     Given I'm an sml portal user on the home page with a cookie banner
    #     When I click the additional cookies link in the header
    #     Then I am taken to the 
    
    # Scenario: View cookies cookies link test
    #     Given I'm an sml portal user on the home page with a cookie banner
    #     When I click the view cookies link in the header
    #     Then I am taken to the "Cookies on the statistical methods library portal" page