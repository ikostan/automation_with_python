Feature: Test that pages have correct content

  Scenario: Blog has correct title
    Given I am on the "blog" page
    Then There is a title shown on the page
    And The title has content "This is the blog page"

  Scenario: Home has correct title
    Given I am on the "home" page
    Then There is a title shown on the page
    And The title has content "This is the home page"

  Scenario: Post has correct title
    Given I am on the "post" page
    Then There is a title shown on the page
    And The title has content "Create post"

  Scenario: Blog page loads the posts
    Given I am on the "blog" page
    And I wait for the posts to load
    Then I can see there is a posts section on the page

  Scenario: User can create a new post
    Given I am on the "post" page
    When I enter "Test Post" in the "title" field
    And I enter "Test Content" in the "content" field
    And I press the submit button
    Then I am on the "blog" page
    Given I wait for the posts to load
    Then I can see there is a post with title "Test Post" in the posts section

