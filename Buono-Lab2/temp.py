import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from load import fromdicttolist, randomSubset
from linearRegression import computeOneDimensional, computeOneDimensionaWITHinterception, computeMultipleDimensional
from linearRegression import computeMeanSquareError, computelinearpredict
from display import oneDimensionalGraph, multiDimensional
from trainingANDtest import dimensionalWithInterception
#point 3
carsSubsetperctraining, carsSubsetperctest = randomSubset(carsSubSetlist, perc, carsSubSetlist)
cars1Dimwithperc = computeOneDimensionaWITHinterception(carsSubsetperctraining)
oneDimensionalGraph(variables, carsSubsetperctraining, cars1Dimwithperc[0], cars1Dimwithperc[1])
#plt.legend()
#plt.show()

# ----compute mean square error ----
predictWithInt = computelinearpredict(carsSubsetperctraining[0], cars1Dimwithperc[0], cars1Dimwithperc[1])
meanWithInt = computeMeanSquareError(carsSubsetperctraining[1], predictWithInt)
print(f"TRAINING - One-dimensional problem with intercept: {meanWithInt}")
print(f"TEST - One-dimensional problem with intercept: {meanWithInt}")

""" TASK 3 - part 1 """ """ TASK 1 - part 2 (mean)"""
print("###-----Test regression model-----###")
perc = 0.10

print("Mean square error of points 1, 3, 4")
# point 1
turkishpercenttraining, turkishpercenttest = randomSubset(turkish, perc, turkish)
turkishpercOneDimensional = computeOneDimensional(turkishSubSet)
oneDimensionalGraph(coordinates, turkishpercenttraining, turkishpercOneDimensional)
#plt.legend()
#plt.show()

# ----compute mean square error ----
predictOneDim = computelinearpredict(turkish[0], turkishpercOneDimensional)     # NOT SURE
meanOneDim = computeMeanSquareError(turkish[1], predictOneDim)                  #NOT SURE
print(f"TRAINING - One-dimensional problem without intercept: {meanOneDim}")
print(f"TEST - One-dimensional problem without intercept: {meanOneDim}")

""" point 3 """
carsSubsetperctraining, carsSubsetperctest = randomSubset(carsSubSetlist, perc, carsSubSetlist)
dimensionalWithInterception(carsSubsetperctraining, variables, "TRAINING")
dimensionalWithInterception(carsSubsetperctest, variables, "TEST")

# point 4
"""DA AGGIUSTAAAAAREEEEEEEE"""
#carsMPG = fromdicttolist(cars, goalLabel)
#carsMultipleperc, carsMPGperc = randomSubset(carsMultipleList, perc, carsMPG) NO SECONDO DATABASE
#carsMultDimperc = computeMultipleDimensional(carsMultipleperc, carsMPGperc)
#
## ----compute mean square error ----
#meanMult = computeMeanSquareError(carsMPGperc, carsMultDimperc) NO DIMENSIONI
#print(f"TRAINING - Multi-dimensional problem: {meanMult}")
#
#multiDimensional(carsMPGperc, carsMultDimperc)