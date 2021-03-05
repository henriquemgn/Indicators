import time
import math

# Just a Sample of values
closePrices = [1,101,102,98,103,97,103,95,103,107,95,97,94,103,107,110,105,100,101,96,94,35]

def SimpleMovingAverage(closePrices, period):
    sumValues = 0
    for i in range(period):
        sumValues+=closePrices[i]
        
    movingAverage = sumValues/period

    print("MA",period,": ", movingAverage)
    return(movingAverage)

SimpleMovingAverage(closePrices,10)
