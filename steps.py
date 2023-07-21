from behave import given, when, then
from datetime import datetime, timedelta


class Account:
    def addBalance(self, amount, symbol, aquisitionTime):
        pass



@given(u'Balance = {"BTC": 100, "USDT": 0}')
@given(u'Holding Period > 1 Year')
def step_impl(context):
    account = Account()
    current_date = datetime.now()
    one_year_ago = current_date - timedelta(days=365)
    account.addBalance(200, "BTC", one_year_ago)

@given(u'Loss Balance is not filled at all')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Loss Balance is not filled at all')


@given(u'I\'m in the money 200 bucks')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I\'m in the money 200 bucks')


@given(u'Price BTC = 1')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Price BTC = 1')


@when(u'Sell Signal is fired')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Sell Signal is fired')


@then(u'Balance = {"BTC":0, "USDT": 300}')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Balance = {"BTC":0, "USDT": 300}')
