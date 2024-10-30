import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from load import fromdicttolist
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
    dimSubset = round(0.1 * len(turkish))
    randomSubset = np.random.permutation(len(turkish))[:dimSubset]
    turkishSubSet = [turkish[e] for e in randomSubset]
    turkishOneDimensional = computeOneDimensional(turkishSubSet)

# point 2 
    oneDimensionalGraph(coordinates, turkishSubSet, turkishOneDimensional, 0)
plt.legend()
#plt.show()

# point 3
cars = pd.read_csv("mtcarsdata-4features.csv")
cars.columns = cars.columns.str.replace(" ", "")
cars = cars.to_dict(orient="records")

#dimSubset = round(len(cars))
#randomSubset = np.random.permutation(len(cars))[:dimSubset]
#carsSubSetdict = [cars[e] for e in randomSubset]


variables = ["weight", "mpg"]
carsSubSetlist = fromdicttolist(cars, variables)

cars1Dimwith = computeOneDimensionaWITHinterception(carsSubSetlist)
oneDimensionalGraph(variables, carsSubSetlist, cars1Dimwith[0], cars1Dimwith[1])
plt.legend()
#plt.show()

carsMultipleDimvar = ["disp", "hp", "weight"]
carsMultipleList = fromdicttolist(cars, carsMultipleDimvar)

goalLabel = ["mpg"]
carsMPG = fromdicttolist(cars, goalLabel)
carsMultDim = computeMultipleDimensional(carsMultipleList, carsMPG)
multiDimensional(carsMPG, carsMultDim)