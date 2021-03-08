#Assume a 5 bar Bollinger band with 2 Deviations, and assume the last five closes were 25.5, 26.75, 27.0, 26.5, and 27.25.
#
#
#Calculate the simple moving average:
#
#
#25.5 + 26.75 + 27.0 + 26.5 + 27.25 = 133.0
#
#133.0 / 5 = 26.6
#
#
#Next, for each bar, subtract 26.6 from the close and square this value:
#
#
#25.5 - 26.6 =	-1.1	squared =	1.21
#26.75 - 26.6 =	0.15	squared =	0.023
#27.0 - 26.6 =	0.4	squared =	0.16
#26.5 - 26.6 =	0.1	squared =	0.01
#27.25 - 26.6 =	0.65	squared =	0.423
#
#Add the above calculated values, divide by 5, and then get the square root of this value to get the deviation value:
#
#
#1.21 + 0.023 + 0.16 + 0.01 + 0.423 = 1.826
#
# 1.826 / 5 = 0.365
#
#Square root of .365 = 0.604
#
#
#The upper Bollinger band would be 26.6 + (2 * 0.604) = 27.808
#
#
#The middle Bollinger band would be 26.6
#
#
#The lower Bollinger band would be 26.6 - (2 * 0.604) = 25.392
import math

			#First calculate the Small Moving Average
lastCloses = [25.5,26.75,27,26.5,27.25]
sumCloses = 0

for i in range(len(lastCloses)):
	sumCloses += lastCloses[i]

SMA = sumCloses/len(lastCloses)
			#Then calculate the Variance so that you can get the Deviation after
Variance = 0
for l in range(len(lastCloses)):
	Variance += ((lastCloses[l]-SMA)**2)

Variance = Variance/5

			#Get the Deviation
Deviation = math.sqrt(Variance)

			#To get the Upper Bollinger Band you add the Deviation times 2
UpperBollingerBand = SMA + (2 * Deviation)
			#To get the Middle Bollinger Band you just got to put the SMA being used
MiddleBollingerBand = SMA
			#To get the Lower Bollinger Band you subtract the Deviation times 2
LowerBollingerBand = SMA - (2 * Deviation)

			#Showing results
print("Upper Bollinger Band: %02f" %UpperBollingerBand)
print("Middle Bollinger Band: %02f" %MiddleBollingerBand)
print("Lower Bollinger Band: %02f" %LowerBollingerBand)