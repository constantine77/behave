Feature: Showing off behave

  Scenario: Run a simple test
    Given we have behave installed
     When we implement 5 tests
     Then behave will test them for us!

  Scenario: Run a record count
    Given Expected Record count for output file
    |input   |
    | 3       |
    Then I will see the record count match input vs output

