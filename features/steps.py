from decimal import Decimal
from behave import given, when, then
from datetime import datetime, timedelta


# Sample data to keep track of the account balance
account_balance = {}
account_unrealized_value = {}
account_accrued_losses = 0

# Helper function to parse "X days" format into timedelta
def parse_days(days_str):
    days = int(days_str.split()[0])
    return timedelta(days=days)


# Helper function to get timedelta representing one year
def short_term_holding_period():
    return timedelta(days=365)

# Step implementations
@given('an account with base currency {currency} and balance')
def step_account_with_balance(context, currency):
    for row in context.table:
        asset = row['Asset']
        amount = Decimal(row['Amount'])
        holding_period = parse_days(row['Holding Period'])
        quote = Decimal(row['Quote'])
        account_balance[asset] = {'amount': amount, 'holding_period': holding_period, 'quote': quote}

@given('current Quotes are')
def step_current_quotes(context):
    account_unrealized_value = {}
    for row in context.table:
        asset = row['Asset']
        quote = Decimal(row['Quote'])
        if asset in account_balance:
            # fill in the blanks
            account_unrealized_value[asset] = {'asset' : asset, 'quote' : quote}

@given('"Accrued Losses" = 0')
def step_accrued_losses(context):
    # If "Accrued Losses" is needed for calculations, implement it here
    account_accrued_losses = 0

@when('Sell Signal is fired')
def step_sell_signal_fired(context):
    for asset, data in account_balance.items():
        if data['holding_period'] >= short_term_holding_period():  # Check if Holding Period > 1 Year (365 days)
            if data['amount'] >= 0:  # Check if there are assets to sell
                data['amount'] = 0
                data['holding_period'] = timedelta(days=0)

@then('the account has Balance of')
def step_account_has_balance(context):
    for row in context.table:
        asset = row['Asset']
        expected_amount = Decimal(row['Amount'])
        expected_holding_period = parse_days(row['Holding Period'])
        expected_quote = Decimal(row['Quote'])
        
        if asset in account_balance:
            assert account_balance[asset]['amount'] == expected_amount
            assert account_balance[asset]['holding_period'] == expected_holding_period, "Holding Period for {} is {} but expected {}".format(asset, account_balance[asset]['holding_period'], expected_holding_period)
            assert account_balance[asset]['quote'] == expected_quote, "Quote for {} is {} but expected {}".format(asset, account_balance[asset]['quote'], expected_quote)
