Feature: Selling Long Term Holdings for Tax-Free Profit
User Persona: German Crypto Trader
User Need: To get a 100% approval to sell Long Term Holdings if they have a tax-free profit.
Background Information:
- In Germany, the Long Term Holding Period for cryptocurrencies is 1 year, and selling after this period guarantees that the profit is tax-free.
- Accrued losses do not impact Long Term Holding Period decisions, as they would not reduce tax-free profit.
- Trading fees are added to the loss balance because they decrease the tax-free profit.
- (Open for discussion) Trading fees also decrease the net profit, but this consideration is separate from a tax strategy.

  Scenario: Approve to sell everything if Long Term Holding Period passed for the entire wallet
    Given a wallet with
      | Asset | Amount | Buy Date       |  Quote |
      | BTC   |      1 |   2020-01-01   |  30100 |
    When asked for tax advice to sell 1 BTC at 30100 USDT on 2021-01-01
    Then I get an approval to Sell 1 BTC


