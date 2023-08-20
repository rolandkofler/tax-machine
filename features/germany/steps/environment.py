from germany.taxmachine import TaxMachine


def before_scenario(context):
    context.taxmachine = TaxMachine()
