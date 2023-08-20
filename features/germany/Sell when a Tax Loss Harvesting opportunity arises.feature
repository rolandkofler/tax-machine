Feature: Sell when a Tax Loss Harvesting opportunity arises.
    In order to reduce my tax burden
    As a German Crypto Trader
    I want to sell my assets when Loss is greater than an absolute value.
    And Ive held the asset for more than x days.
    And I want to sell it early in the short term holding period, because then I can open a position sooner for potential long term zero tax gains.

    Scenario: Send Sell Signal when loss acrued and time held are met.
        Given we are In The Market
        And Loss is greater then 500 dollars
        When we have held the asset for more then 30 days 
        Then send a Sell Signal to the Tax Machine




    
Comment: The easeast way is if threat an exchange account as gated. 
    Only money and no assets should get in or out. 
    But we dont want to do that in order to keep the tax opportunities of old assets. 



        
