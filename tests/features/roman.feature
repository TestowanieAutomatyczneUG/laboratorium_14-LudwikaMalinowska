Feature: Converting numbers to roman

  Scenario Outline: <n> is roman <roman>
    Given <n> is given
    Then the output is <roman>

    Examples:
      | n    | roman |
      | 1    | I     |
      | 49   | XLIX  |
      | 575  | DLXXV |
      | 1024 | MXXIV |

    