Feature: Sell when a Tax Loss Harvesting opportunity arises.
    In order to reduce my tax burden
    As a Crypto Trader
    I want to sell my assets when Loss is greater than an absolute value.
    And Ive held the asset for more than x days.

Feature:
    As a German Crypto Trader
    I want to sell my assets when a Tax Loss Harvesting opportunity arises.
    But I dont want to sell them too close to the end of the short term holding period.
    And I want to sell it early in the short term holding period.
    Therefore I attribute a propensity of selling to each day in the short term holding period.
     


    Scenario: Send Sell Signal when loss acrued and time held are met. 
        Given we are In The Market
        And Loss is greater then 500 dollars
        When we have held the asset for more then 30 days 
        Then send a Sell Signal to the Tax Machine

Feature: Sell on Sell Signal if it is worth it.
    In order to only sell when it is worth it
    As a Crypto Trader
    I want to sell my assets only if the capital gain reaches a certain threshold.

Feature: Sell without moving the market
    In order to not move the market
    As a Crypto Trader
    I want to sell my assets sliced up in small chunks over time.

Feature: Book in new assets with its own cost basis and time held.
    In order to make per account tax calculations possible
    As a Crypto Trader
    I want to book in new assets with their own cost basis and time held.
    
Comment: The easeast way is if threat an exchange account as gated. 
    Only money and no assets should get in or out. 
    But we dont want to do that in order to keep the tax opportunities of old assets. 



        
