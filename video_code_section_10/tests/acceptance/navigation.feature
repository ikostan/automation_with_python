Feature: Test navigation between pages we
         can have a longer description
         that can span a few lines

  Scenario: Homepage can go to Blog
    Given I am on the "home" page
    When I click on the "Go to blog" link
    Then I am on the "blog" page

  Scenario: Blog can go to Homepage
    Given I am on the "blog" page
    When I click on the "Go to home" link
    Then I am on the "home" page

  Scenario: Post can go to Blog
    Given I am on the "post" page
    When I click on the "Back to blog" link
    Then I am on the "blog" page

