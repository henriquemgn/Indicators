def ATR(high,low,period):
	sumPrior = 0
	for i in range(period):
		sumPrior += (high[i]-low[i])

	ATR = sumPrior/(period)

	return ATR