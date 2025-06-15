Feature: Magento Customer Login

  Scenario: Successful login
    Given I open the Magento homepage
    When I click the "Sign In" link
    And I enter email "pandajagannath964@gmail.com" and password "Chiku@123"
    Then I should see a welcome message with my name