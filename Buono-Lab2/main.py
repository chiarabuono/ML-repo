import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from load import fromdicttolist, randomSubset
from linearRegression import computeOneDimensional, computeOneDimensionaWITHinterception, computeMultipleDimensional
from display import oneDimensionalGraph, multiDimensional

turkish = pd.read_csv("turkish-se-SP500vsMSCI.csv")

# display
coordinates = turkish.columns
axisX = turkish[coordinates[0]].tolist()
axisY = turkish[coordinates[1]].tolist()
#plt.scatter(axisX, axisY)
#plt.show()

""" TASK 1 """
# point 1
turkish = turkish.values.tolist()
turkishOneDimensional = computeOneDimensional(turkish)
oneDimensionalGraph(coordinates, turkish, turkishOneDimensional, 0)
plt.legend()
#plt.show()

# point 2

for e in range(2):
    turkishSubSet = randomSubset(turkish, 0.1)
    turkishOneDimensional = computeOneDimensional(turkishSubSet)

# point 2 
    oneDimensionalGraph(coordinates, turkishSubSet, turkishOneDimensional, 0)
plt.legend()
#plt.show()

# point 3
cars = pd.read_csv("mtcarsdata-4features.csv")
cars.columns = cars.columns.str.replace(" ", "")
cars = cars.to_dict(orient="records")

variables = ["weight", "mpg"]
carsSubSetlist = fromdicttolist(cars, variables)

cars1Dimwith = computeOneDimensionaWITHinterception(carsSubSetlist)
oneDimensionalGraph(variables, carsSubSetlist, cars1Dimwith[0], cars1Dimwith[1])
plt.legend()
#plt.show()

# point 4
carsMultipleDimvar = ["disp", "hp", "weight"]
carsMultipleList = fromdicttolist(cars, carsMultipleDimvar)

goalLabel = ["mpg"]
carsMPG = fromdicttolist(cars, goalLabel)
carsMultDim = computeMultipleDimensional(carsMultipleList, carsMPG)
multiDimensional(carsMPG, carsMultDim)

""" TASK 3 - part 1 """
perc = 0.05
# point 1
turkishpercent = randomSubset(turkish, perc)
turkishpercOneDimensional = computeOneDimensional(turkishSubSet)

oneDimensionalGraph(coordinates, turkishpercent, turkishpercOneDimensional, 0)
plt.legend()
plt.show()

# point 3
carsSubsetperc = randomSubset(carsSubSetlist, perc)
cars1Dimwithperc = computeOneDimensionaWITHinterception(carsSubsetperc)
oneDimensionalGraph(variables, carsSubsetperc, cars1Dimwithperc[0], cars1Dimwithperc[1])
plt.legend()
plt.show()

# point 4
carsMultipleperc = randomSubset(carsMultipleList, perc)
carsMPG = fromdicttolist(cars, goalLabel)
carsMultDimperc = computeMultipleDimensional(carsMultipleperc, carsMPG)
multiDimensional(carsMPG, carsMultDimperc)

""" TASK 1 - part 2"""
