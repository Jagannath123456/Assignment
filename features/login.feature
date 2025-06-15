Feature: Magento Customer Login

  Scenario Outline: Login attempts with various credentials
    Given I open the Magento homepage
    When I click the "Sign In" link
    And I enter email "<email>" and password "<password>"
    Then I should see outcome "<outcome>"

  Examples:
    | email                             | password      | outcome               |
    | pandajagannath964@gmail.com       | Chiku@123     | success               |
    | invalid@user.com                  | Chiku@123     | invalid_credentials   |
    | pandajagannath964@gmail.com       | wrongPass     | invalid_credentials   |
    | ""                                | Chiku@123     | required_email        |
    | pandajagannath964@gmail.com       | ""            | required_password     |
    | MIXED.CASE@USER.COM               | Chiku@123     | success               |
    | user@softwaretestingboard.com     | short         | weak_password         |
    | user@softwaretestingboard         | Chiku@123     | invalid_email_format  |
    | ""                                | ""            | required_both         |
