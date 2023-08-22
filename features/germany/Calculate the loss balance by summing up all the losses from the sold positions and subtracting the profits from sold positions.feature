Feature: calculate the loss balance by summing up all the losses from the sold positions and subtracting the profits from sold positions.
    In order to know how much loss I can deduce from my taxes, as a German crypto trader, I want to calculate the taxable loss balance.
    Scenario: calculate the loss balance for a single position
        Given a wallet with a single position.
        | Asset | Amount | Buy Date               |  Quote |
        | BTC   |      1 |   2020-01-01T10:00:30  |  30100 |
        When I book in a Sale of 1 BTC for 30000 EUR on 2020-01-01T10:00:31
        Then the loss balance is 100 EUR
