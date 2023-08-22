Feature: Sell if loss balance covers the profit.
  As a German Crypto Trader,
    I want to be advised to sell a FIFO position even in the short term period, if the loss balance covers the profit.
  User Persona: German Crypto Trader
  User Need:  To be advised on when to sell a FIFO position, even in the short term, if the loss balance covers the profit.
  Acceptance Criteria:
    The system should identify the earliest trade within the wallet and track it as the first position to be sold (FIFO).
    The system should calculate the loss balance by summing up all the losses from the sold positions and subtracting the profits from sold positions.
    The system should notify the user to sell a FIFO position if the loss balance is greater than or equal to the profit.
    The system should consider the cost basis of each individual wallet for the FIFO calculation and should not include trades outside of the wallet.
  Background Information:
  - In German tax accounting, FIFO is used, where the earliest trade made is the first one to be sold.
  - In German tax accounting, each wallet has its own cost basis, and trades outside of the wallet are not considered for FIFO calculation.
  - Loss Balance is calculated as the sum of all sold positions with a loss minus the sum of all sold positions with a profit.
  - Taxes are always accounted in the domestic currency of tax residency, for Germany it is the Euro.
  - Trading fees are added to the loss balance because they decrease the tax-free profit. Trading fees do not affect the tax advice (really and why?).

  Scenario: Advising the Trader to Sell when Loss Balance Covers the Profit
      Given a wallet with multiple FIFO positions.
        | Asset | Amount | Buy Date               |  Quote |
        | BTC   |      1 |   2020-01-01T10:00:30  |  30100 |
        | BTC   |      2 |   2020-01-01T12:00:30  |  30200 |
        | BTC   |      3 |   2020-01-01T14:30:00  |  30100 |
      And the trader has a loss balance of 100 EUR.
      When the trader considers selling 6 BTC at 30200 EUR on 2020-01-02T10:00:00.
      Then the tax machine should show the trader the following taxation table
        | Asset | Amount | Holding Period   |  Price Diff | Tax Base|
        | BTC   |      1 |     PT23H59M30S   |      100 EUR|    0 EUR |
        | BTC   |      2 |     PT21H59M30S   |        0 EUR|    0 EUR |
        | BTC   |      3 |     PT19H30M      |      100 EUR|  300 EUR |

  ##scenario 2: No Advice to Sell when Loss Balance Does Not Cover the Profit
  ##    Given a German Crypto Trader with multiple crypto positions in a wallet.
  ##    And the trader has a loss balance that does not cover the profit.
  ##    When the trader considers selling a position.
  # Then the system should not advise the trader to sell the FIFO position.