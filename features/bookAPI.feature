# Created by federicobersani at 02/06/22
Feature: verify if Books are added and deleted using API
  # Enter feature description here

  @smoke
  Scenario: verify AddBook API functionality
    Given the Book details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then book is successfully added


  @regression
  Scenario Outline: verify AddBook API functionality
    Given the Book details with <isbn> and <aisle>
    When we execute the AddBook PostAPI method
    Then book is successfully added
    Examples:
      |isbn  |aisle |
      |fdfee |8908  |
      |prom  |9034  |
