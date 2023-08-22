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
        # create a new account balance for the asset if it does not exist
        if asset not in self.account_balance:
            self.account_balance[asset] = []
        # add a row to the account balance
        self.account_balance[asset].append(
            {
                "amount": amount,
                "buy_date": buy_date,
                "quote": quote,
            }
        )

    # deprecated
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

    def calculate(
        self,
        order_type,
        amount: Decimal,
        currency,
        price: Decimal,
        domestic_currency,
        when: datetime,
        fee: Decimal,
    ):
        """
        :param order_type: buy or sell
        :param amount: how much to buy or sell
        :param currency: in which currency to buy or sell
        :param price: price in quote currency
        :param domestic_currency: tax fiat currency
        :param when: planned datetime of the transaction to calculate the tax for
        :param fee: transaction fee in domestic currency
        :return: taxation table for different FIFO positions needed for the transaction
        """

        remainder = Decimal(amount)
        # create a copy of the account balance
        account_balance = self.account_balance[currency].copy()
        # sort the account balance by buy_date
        account_balance.sort(key=lambda x: x["buy_date"])
        taxation_table = []
        for row in account_balance:
            # check if the position is older than 'when' assuming all positions are sorted by buy_date
            time = datetime.fromisoformat(when)
            if row["buy_date"] > time:
                break
            if remainder < 0:
                break
            remainder = remainder - row["amount"]
            value = Decimal(amount)
            if value >= row["amount"]:
                value = row["amount"]
            holding_period = time - row["buy_date"]
            price_difference = Decimal(price) - row["quote"]
            # calculate the tax base for the position
            brutto_tax_base = value * price_difference
            # deduce the loss balance from the tax base and reduce the loss balance by that amount
            if brutto_tax_base < self.account_accrued_losses:
                netto_tax_base = Decimal(0)
                self.account_accrued_losses -= brutto_tax_base
            else:
                netto_tax_base = brutto_tax_base - self.account_accrued_losses
                self.account_accrued_losses = Decimal(0)
                # and add them to the taxation table
                taxation_table.append(
                    {
                        "Asset": currency,
                        "Amount": row["amount"],
                        "Holding Period": holding_period,
                        "Price Diff": price_difference,
                        "Tax Base": netto_tax_base,
                    }
                )
        return taxation_table

    def post_sell(
        self,
        amount: Decimal,
        currency: str,
        when: datetime,
        price: Decimal,
        fees: Decimal,
    ):
        """
        :param amount: how much to buy or sell
        :param currency: in which currency to buy or sell
        :param when: planned datetime of the transaction to calculate the tax for
        :param price: price in quote currency
        :param quote: price in quote currency
        :param fees: transaction fee in domestic currency
        :return: taxation table for different FIFO positions needed for the transaction
        """
        # calculate the taxation table
        taxation_table = self.calculate(
            "sell",
            amount,
            currency,
            price,
            "EUR",
            when,
            fees,
        )
        # extract the tax base from the taxation table
        tax_base = sum([row["Tax Base"] for row in taxation_table])
        # add to the loss balance
        self.account_accrued_losses += tax_base
