
Feature: Counting isbn control number

  Scenario Outline: Checking if isbn number is valid
    Given given <isbn_number>
    When the number is checked
    Then the result is <result>

    Examples:
      | isbn_number         | result    |
      | 978-3-16-148410-0   | True      |
      | 978-3-16-14840-0    | False     |
      | 978-3-16-1484110-0  | False     |
      | 978-3-16-148412-0   | False     |
