from sismic.interpreter import Interpreter
from sismic.io import import_from_yaml
from sismic.model import Statechart

i: int=0

def logState(step):
    global i
    i += 1
    print (f"----- step #{i} --------------------------")
    for attribute in ['event', 'transitions', 'entered_states', 'exited_states', 'sent_events']:
        print('{}: {}'.format(attribute, getattr(step, attribute)))

    print(f'After step #{i}:', interpreter.configuration)
# Decision: Implement strategy to align balances to the bot's current state.
#
# Reasoning: This strategy provides an opportunity to maximize market returns by being more responsive
# to market conditions. With this implementation, as soon as new assets are added or the market state
# changes, the bot will align the asset holdings accordingly. This ensures assets are not left idle and
# are always working to generate returns based on the bot's current market view.
#
# While this strategy might incur slightly more transaction costs due to increased trading frequency, the potential
# benefits in terms of improved asset utilization and responsiveness to market changes outweigh the costs.
# In volatile markets, this strategy could provide better performance by promptly reacting to market signals.


statechart = import_from_yaml(text = '''
statechart:
  name: Deutschland Maschine
  preamble: |
    wePreferToWait = True
  root state: 
    name: Yet another Deutschland Maschine
    initial: Out of the Market
    states: 
      - name: Out of the Market
        transitions: 
          - target: In the Market
            event: "buy signal fired"
          - target: Slice and Sell
            event: "sell signal fired"
            guard: not wePreferToWait
          - target: Wait for Prescribed Holding Period
            event: "sell signal fired"
            guard: wePreferToWait
        states:
          - name: Slice and Sell
          - name: Wait for Prescribed Holding Period
            transitions:
             - target: Slice and Sell
               event: Holding Period is over    
      - name: In the Market
        transitions:
          - target: Out of the Market
            event: sell signal fired
'''
                              )
assert isinstance(statechart, Statechart)
# Create an interpreter for this statechart
interpreter = Interpreter(statechart)


step1 = interpreter.execute_once()
logState(step1)

step2 =interpreter.queue("sell signal fired").execute_once()
logState(step2)

step3 =interpreter.queue("sell signal fired").execute_once()
logState(step3)

