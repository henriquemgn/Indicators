from datetime import datetime
high = []#put highs to test
low = []#put lows to test

#just to have it initiated 
IchimokuCloudA = []
IchimokuCloudB = []

def IchimokuCloud(high,low,IchimokuCloudA,IchimokuCloudB):
	IchimokuCloudA = []
	IchimokuCloudB = []
	conversion = []
	base = []
	counter = 26
	while counter >= 0:
		period9High = 0
		period9Low = 0
			
		period26High = 0
		period26Low = 0
			
		period52High = 0
		period52Low = 0
            #Gets highest and lowest value from the last 9 periods
		for i in range(9):
			if high[i+counter] > period9High:
				period9High = high[i+counter]
			if low[i+counter] < period9Low or period9Low == 0:
				period9Low = low[i+counter]

            #Gets highest and lowest value from the last 26 periods
		for x in range (26):
			if high[x+counter] > period26High:
				period26High = high[x+counter]
			if low[x+counter] < period26Low or period26Low == 0:
				period26Low = low[x+counter]

            #Gets highest and lowest value from the last 52 periods
		for y in range (52):
			if high[y+counter] > period52High:
				period52High = high[y+counter]
			if low[y+counter] < period52Low or period52Low == 0:
				period52Low = low[y+counter]

	    #Calculates Conversion and Base Lines
		conversionLine = (period9High + period9Low) / 2
		baseLine = (period26High + period26Low) / 2

	    #Calculates the leading span
		leadingSpanA = (conversionLine + baseLine) / 2
		leadingSpanB = (period52High + period52Low) / 2

            #appends it to all the cloud values for the 26 counter
		IchimokuCloudA.append(leadingSpanA)
		IchimokuCloudB.append(leadingSpanB)

		if IchimokuCloudA[0] == 0:
			IchimokuCloudA.remove(0)
		if IchimokuCloudB[0] == 0:
			IchimokuCloudB.remove(0)
		counter -= 1
		
	return IchimokuCloudA, IchimokuCloudB,conversionLine,baseLine


