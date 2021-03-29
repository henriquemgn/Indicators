##########################
# Linnearly Weighted Moving Average
# - calculates Moving Average with a linear weight (duh heh) for example:
# 20 periods would be currentValue*20 + pastValue*19 ..etc and then dividing but the sum of the multiplications in this case 210
#
# Hull's Moving Average
# Developed by Alan Hull in 2005, this indicator makes use of weighted moving averages to prioritize more recent values and greatly reduce lag. source: stockcharts
#
# Code:
# closedPrices in closedPrices[0] is current and closedPrices[1] is previous etc
# period is the length of the Moving Average
# in usual Hull's Moving Average you wouldn't use math.floor, you would round to the nearest int value, using math.round
# but i like using floor :P
#
# Comment:
# It was really hard to understand HMA, I went from SMA to EMA with no problem and then HMA got me stuck for a while, but was really satisfying to make it work
# with love, Magno
##########################

import math

def calculate_lwma(closedPrices,period):
	sum_multipliers = 0
	sum_weights = 0
	for i in range(period):
		sum_multipliers += (closedPrices[0+i] * (period-i))
		sum_weights += (period-i)
    
	LWMA = sum_multipliers/sum_weights
	
	return LWMA

def HMA(closedPrices,period):
	raw_HMA = []
	for i in range(math.floor(math.sqrt(period))):
		raw_HMA.append((2 * calculate_lwma(closedPrices[0+i:],math.floor(period/2))) - calculate_lwma(closedPrices[0+i:],period))
	
	HMA = calculate_lwma(raw_HMA,math.floor(math.sqrt(period)))
	return HMA
