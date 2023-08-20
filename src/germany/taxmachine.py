from _decimal import Decimal
from datetime import datetime


class Approval:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency


class TaxMachine:
    def __init__(self):
        self.account_balance = {}
        self.account_accrued_losses = Decimal(0)

    def post_buy(self, asset, amount, buy_date, quote):
        self.account_balance[asset] = {
            "amount": amount,
            "buy_date": buy_date,
            "quote": quote,
        }

    def approve(
        self,
        sell,
        amount: Decimal,
        currency,
        price: Decimal,
        quote_currency,
        date: datetime,
        fees: Decimal,
    ) -> Approval or None:
        return Approval(1, "BTC")
