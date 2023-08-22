import isodate
from _decimal import Decimal
from datetime import datetime, timedelta
from decimal import Decimal

from behave import *

from germany.taxmachine import TaxMachine


# Step implementations
@given("a wallet with multiple FIFO positions.")
@given("a wallet with")
@given("a wallet with a single position.")
def step_account_with_balance(context):
    """
    :type context: behave.runner.Context
    """
    context.taxmachine = TaxMachine()
    taxmachine = context.taxmachine
    for row in context.table:
        asset = row["Asset"]
        amount = Decimal(row["Amount"])
        buy_date_str = row["Buy Date"]
        # Assuming row["Buy Date"] contains a string representing the datetime in ISO format, e.g. "2019-01-01T00:00:00"
        buy_datetime = datetime.strptime(
            buy_date_str, "%Y-%m-%dT%H:%M:%S"
        )  # Adjust the format according to your input string

        quote = Decimal(row["Quote"])
        taxmachine.post_buy(asset, amount, buy_datetime, quote)


@when(
    "asked for tax advice to {sell} {amount} {currency} at {price} {quote_currency} on {sell_date} "
)
@when(
    "the trader considers {sell} {amount} {currency} at {price} {quote_currency} on {sell_date}."
)
def step_asked_for_tax_advice(
    context, sell, amount, currency, price, quote_currency, sell_date
):
    if sell == "selling":
        sell = "sell"  # allows more natural language
    taxmachine: TaxMachine = context.taxmachine
    context.taxation_table = taxmachine.calculate(
        sell,
        Decimal(amount),
        currency,
        Decimal(price),
        quote_currency,
        datetime.strptime(sell_date, "%Y-%m-%dT%H:%M:%S"),
        Decimal(0),
    )


@then("I get an approval to Sell {amount} {currency}")
def step_impl(context, amount, currency):
    approved = context.approved
    assert approved.amount == Decimal(amount) and approved.currency == currency


@step("the trader has a loss balance of {amount} EUR.")
def step_impl(context, amount):
    """
    :type context: behave.runner.Context
    """
    context.taxmachine.account_accrued_losses = Decimal(amount)


@then("the tax machine should show the trader the following taxation table")
def the_tax_machine_should_show_tax_table(context):
    assert context.taxation_table is not None
    for rowShould, rowIs in zip(context.table, context.taxation_table):
        assert rowShould["Asset"] == rowIs["Asset"]
        assert Decimal(rowShould["Amount"]) == rowIs["Amount"], (
            "amount should be "
            + rowShould["Amount"]
            + " but is "
            + str(rowIs["Amount"])
        )
        holding_period = rowIs["Holding Period"]
        # parse rowShould["Holding Period"] as a string of ISO 8601 duration and convert to timedelta
        holding_periodShould = isodate.parse_duration(
            rowShould["Holding Period"].strip()
        )
        assert holding_period == holding_periodShould, (
            "holding period should be "
            + str(holding_periodShould)
            + " but is "
            + str(holding_period)
        )


@when("I book in a Sale of {amount} {currency} for {price} EUR on {when}")
def step_impl(context, amount: Decimal, currency, price: Decimal, when: datetime):
    """
    :type context: behave.runner.Context
    """
    taxmachine: TaxMachine = context.taxmachine
    taxmachine.post_sell(amount, currency, when, price, Decimal(0))


@then("the loss balance is {amount} EUR")
def step_impl(context, amount: Decimal):
    """
    :type context: behave.runner.Context
    """
    assert context.taxmachine.account_accrued_losses == Decimal(amount), (
        "loss balance should be "
        + str(amount)
        + " but is "
        + str(context.taxmachine.account_accrued_losses)
    )
