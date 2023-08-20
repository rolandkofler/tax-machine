Feature: Sell if Long Term Holding Period passed
  As a German Crypto Trader,
  I want to get an 100% approval to sell my Long Term Holdings and I have a tax free profit.
  The Long Term Holding Period is 1 year for crypto currencies and guarantees that the profit is tax free.
  Accrued Losses do not play into Long Term Holding Period decisions as they would not reduce the tax free profit.
  Trading fees will decrease the tax free profit. The net profit therefore deduces projected trading fees of x% order volume.
  Scenario: Approve to sell everything if Long Term Holding Period passed for the entire wallet
    Given an account with Base Currency USDT and balance
      | Asset | Amount | Buy Date       |  Quote |
      | BTC   |      1 |   2020-01-01   |  30100 |
    When asked for tax advice to sell 1 BTC at 30100 USDT on 2021-01-01 with trading fees of 0.1%
    Then I get an approval to Sell 1 BTC
