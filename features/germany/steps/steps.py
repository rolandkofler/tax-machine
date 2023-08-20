import datetime
from _decimal import Decimal
from datetime import datetime
from decimal import Decimal

from behave import *

from germany.taxmachine import TaxMachine


# Step implementations
@given("an account with base currency {currency} and balance")
def step_account_with_balance(context, currency):
    context.taxmachine = TaxMachine()
    taxmachine = context.taxmachine
    for row in context.table:
        asset = row["Asset"]
        amount = Decimal(row["Amount"])
        buy_date_str = row[
            "Buy Date"
        ]  # Assuming row["Buy Date"] contains a string representing the date
        buy_date = datetime.strptime(
            buy_date_str, "%Y-%m-%d"
        )  # Adjust the format according to your input string

        quote = Decimal(row["Quote"])
        taxmachine.post_buy(asset, amount, buy_date, quote)


@when(
    "asked for tax advice to {sell} {amount} {currency} at {price} {quote_currency} on {sell_date} with trading fees of {trading_fees}%"
)
def step_asked_for_tax_advice(
    context, sell, amount, currency, price, quote_currency, sell_date, trading_fees
):
    context.approved = context.taxmachine.approve(
        sell,
        amount,
        currency,
        price,
        quote_currency,
        datetime.strptime(sell_date, "%Y-%m-%d"),
        Decimal(trading_fees) / 100,
    )


@then("I get an approval to Sell {amount} {currency}")
def step_impl(context, amount, currency):
    approved = context.approved
    assert approved.amount == Decimal(amount) and approved.currency == currency
