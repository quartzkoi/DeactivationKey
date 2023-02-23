import numpy as np

# Stores line from packet_base/packet_weight as individual variables
packetBase = np.genfromtxt('packet_base.txt', delimiter=',')
packetWeight = np.genfromtxt('packet_weight.txt', delimiter=',')

# converts the arrays into a usable format
numColumns = 8
numRows = packetBase.size//numColumns
packetBase = packetBase.reshape(numRows, numColumns)
packetWeight = packetWeight.reshape(numRows, numColumns)

# multiplies both arrays
multData = packetBase * packetWeight

# finds the min, max and mean for each row
minValue = np.amin(multData, axis=1)
maxValue = np.amax(multData, axis=1)
meanValue = np.mean(multData, axis=1)

# calculates a new array from min, max and mean
newArray = (maxValue - meanValue) * minValue

# Gets the Array's Sum, then calculates the remainder
sumArray = np.sum(newArray)
remainder = sumArray % 4096
roundedAnswer = remainder//1


print(roundedAnswer)