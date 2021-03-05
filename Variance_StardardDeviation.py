import time
import math

# Just a Sample of values
closePrices = [1,101,102,98,103,97,103,95,103,107,95,97,94,103,107,110,105,100,101,96,94,35]

def Variance(closePrices):
    # First calculate the Mean Average
    i = 1
    sumValues = 0
    Variance = 0
    while i < 21:
        sumValues += closePrices[i]
        i+=1
    i = 1
    meanAvg = sumValues/20
    print("Mean Avg: ", meanAvg)
    #Then calculate the variance by subtracting the mean average from each value of the sample and then multiply it by itself
    #Do it with all values and make a sum of all of them
    while i < 21:
        Variance += (closePrices[i]-meanAvg)**2
        i+=1

    Variance = Variance/20
    
    return(Variance)

def StandardDeviation(Variance):
    #Calculate the Standand Deviation by getting the square root of the Variance
    standardDev = math.sqrt(Variance)

    return(standardDev)

variance = Variance(closePrices)
standardDeviation = StandardDeviation(variance)

print("Variance: ", variance, "\nStanadard Deviation",standardDeviation)
