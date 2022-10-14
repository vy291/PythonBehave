Feature: E2E test for standard user

  @E2E
  Scenario Outline: Standard user should login successfully, complete checkout and logout
    Given we visit login page
    When we put username "<username>" on login page
    And we put password "<password>" on login page
    And we click submit button on login page
    Then it should login successfully

    When we add new item "<itemName>" from inventory
    And cart icon should be updated
    And we visit cart page
    Then selected item "<itemName>" should be added in shopping cart

    When we click check out button on checkout page
    And we put checkout information "<firstName>" "<lastName>" "<zipCode>" on checkout page
    And we click continue button on checkout page
    And we click finish button on checkout page
    Then it should confirm the checkout is completed

    When we click log out on left menu page
    Then it should logout successfully and back to login page

    Examples:
      | username      | password     | itemName              | firstName | lastName | zipCode |
      | standard_user | secret_sauce | Sauce Labs Backpack   | John      | Smith    | 123     |
      | standard_user | secret_sauce | Sauce Labs Bike Light | Tony      | Stark    | 456     |


  @E2E
  Scenario Outline: Get data from data file
    Given we visit login page
    When we put username on login page from data file "<fileName>"
    And we put password on login page from data file "<fileName>"
    And we click submit button on login page
    Then it should login successfully

    Examples:
      | fileName          |
      | standardUser.json |

  @E2E
  Scenario Outline: Login with invalid credential
    Given we visit login page
    When we put username "<username>" on login page
    And we put password "<password>" on login page
    And we click submit button on login page
    Then it should have error when login with wrong credential

    Examples:
      | username      | password |
      | standard_user | invalid  |