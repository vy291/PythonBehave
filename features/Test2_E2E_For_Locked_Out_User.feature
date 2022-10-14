Feature: E2E test for locked out user

  @E2E
  Scenario Outline: Locked out user should unable to login
    Given we visit login page
    When we put username "<username>" on login page
    And we put password "<password>" on login page
    And we click submit button on login page
    Then it should have error when login with locked out user

    Examples:
      | username        | password     |
      | locked_out_user | secret_sauce |


  @E2E
  Scenario Outline: Get data from data file
    Given we visit login page
    When we put username on login page from data file "<fileName>"
    And we put password on login page from data file "<fileName>"
    And we click submit button on login page
    Then it should have error when login with locked out user

    Examples:
      | fileName           |
      | lockedOutUser.json |