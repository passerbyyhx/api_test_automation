@allure.label.epic:TestAPIDemo
Feature: Test API Demo

  @allure.label.story:Demo
  Scenario: Demo
    When I access the API for 9 day weather
    Then I should see the status is OK
    And I should see the relative humidity data for the day after tomorrow