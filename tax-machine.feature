Feature: Sell if no brainer
  On a Sell signal if
    (1) the Holding Period of 1 year has passed or
    (2) our loss balance allows for a tax free sell
    (3) and I'm in the money over 200 bucks
  we sell

  Scenario: Sell on signal if prescribed Holding Period passed
    Given Holding Period > 1 Year
    And Loss Balance is not filled at all
    And I'm in the money 200 bucks
    And Balance = {"BTC": 100, "USDT": 0}
    And Price BTC = 1
    When Sell Signal is fired
    Then Balance = {"BTC":0, "USDT": 300}

