#######################
# Here I used the Simple Moving Average of the period as the previous EMA
# which probably isn't the best but it is all I got
# Not much else to say really
# I didn't quite understand how EMA works but there it is 
#######################

def calculate_ema(opening_prices ,closing_prices, period):

    previous_EMA = SimpleMovingValue(closing_prices , period)
    
    constant = (2 / (period + 1))
    current_EMA = (closing_prices[0] * constant) + (previous_EMA * (1 - constant))
    
    return (current_EMA)
