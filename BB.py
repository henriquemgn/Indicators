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
