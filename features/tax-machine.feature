Feature: Sell if no brainer
  On a Sell signal if
    (1) the Long Term Holding Period of 1 year has passed or
    (2) our loss balance allows for a tax free sell
    (3) and I'm in the money over 200 bucks
  we sell

  Scenario: Sell on signal if Long Term Holding Period passed
    Given an account with base currency USDT and balance
      | Asset | Amount | Holding Period |  Quote |
      | BTC   |      1 |       366 days |  30100 |
      | USDT  |      0 |         0 days |      1 |
    And "Accrued Losses" = 0
    And current Quotes are
      | Asset | Quote  |
      | BTC   |  30300 |
    When Sell Signal is fired
    Then the account has Balance of
      | Asset | Amount | Holding Period |  Quote |
      | BTC   |      0 |         0 days |  30300 |
      | USDT  |  30300 |         0 days |      1 |

