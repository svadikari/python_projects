Feature: Product Validations

  Scenario: Create Product Item
    Given Item payload is prepared
    When Item create call initiated
    Then Item is persisted and service returns with 201 status


  Scenario Outline: Fetch Product Detail
    Given There are give products exists for <product_id>
    When Product fetch call initiated for <product_id>
    Then Product service responds with <status_code> status

    Examples:
      | product_id | status_code |
      | 1          | 200         |
      | 1000       | 404         |