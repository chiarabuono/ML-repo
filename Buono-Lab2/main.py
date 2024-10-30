import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from linearRegression import computeOneDimensional, computeOneDimensionaWITHinterception
from display import oneDimensionalGraph

turkish = pd.read_csv("turkish-se-SP500vsMSCI.csv")

# display
coordinates = turkish.columns
axisX = turkish[coordinates[0]].tolist()
axisY = turkish[coordinates[1]].tolist()
#plt.scatter(axisX, axisY)
#plt.show()

# point 1
turkish = turkish.values.tolist()

for e in range(2):
    dimSubset = round(0.1 * len(turkish))
    randomSubset = np.random.permutation(len(turkish))[:dimSubset]
    turkishSubSet = [turkish[e] for e in randomSubset]
    turkishOneDimensional = computeOneDimensional(turkishSubSet)

# point 2 
    oneDimensionalGraph(turkishSubSet, turkishOneDimensional)
plt.legend()
#plt.show()

# point 3
cars = pd.read_csv("mtcarsdata-4features.csv")
cars.columns = cars.columns.str.replace(" ", "")
cars = cars.to_dict(orient="records")

dimSubset = round(0.1 * len(cars))
randomSubset = np.random.permutation(len(cars))[:dimSubset]
carsSubSetdict = [cars[e] for e in randomSubset]

carsSubSetlist = []
variables = ["mpg", "weight"]
for e in carsSubSetdict:
    element = []
    for key in variables:
        if key in e: 
            element.append(e[key])
    carsSubSetlist.append(element)

