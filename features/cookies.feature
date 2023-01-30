# Cookie feature tests for both setting and changing cookie preferences

Feature: Cookie banner tests
    Scenario: Accept cookies test
        Given I'm an sml portal user on the home page with a cookie banner
        When I click the accept cookies button in the header
        Then The cookie banner displays "You have accepted all additional cookies. You can change your cookie preferences at any time."

    Scenario: Reject cookies test
        Given I'm an sml portal user on the home page with a cookie banner
        When I click the reject cookies button in the header
        Then The cookie banner displays "You have rejected all additional cookies. You can change your cookie preferences at any time."
    
    Scenario: Additional cookies link test
        Given I'm an sml portal user on the home page with a cookie banner
        When I click the additional cookies link in the header
        Then I am taken to the "Cookies on the statistical methods library portal" page
    
    Scenario: View cookies cookies link test
        Given I'm an sml portal user on the home page with a cookie banner
        When I click the view cookies link in the header
        Then I am taken to the "Cookies on the statistical methods library portal" page

    Scenario: I change the cookie settings to enabled
        Given I am on the cookies page where cookies are already disabled
        When I change my settings to enable cookies
        Then The cookies are enabled

    Scenario: I change the cookie settings to disabled
        Given I am on the cookies page where cookies are already enabled
        When I change my settings to disable cookies
        Then The cookies are disabled