import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from load import fromdicttolist, randomSubset, divideTrainingandTestRandomly
from linearRegression import computeOneDimensional, computeOneDimensionaWITHinterception, computeMultipleDimensional
from linearRegression import computeMeanSquareError, computelinearpredict, wMultipleDimensional
from display import oneDimensionalGraph, multiDimensional

turkish = pd.read_csv("turkish-se-SP500vsMSCI.csv")

coordinates = turkish.columns

""" TASK 1 """
print("###-----Fit a linear regression model-----###")
# point 1
turkish = turkish.values.tolist()
turkishOneDimensional = computeOneDimensional(turkish)
oneDimensionalGraph(coordinates, turkish, turkishOneDimensional)
plt.legend()
plt.show()

# point 2

for e in range(5):
    turkishSubSet = randomSubset(turkish, 0.1)
    turkishOneDimensional = computeOneDimensional(turkishSubSet)

# point 2 
    oneDimensionalGraph(coordinates, turkishSubSet, turkishOneDimensional)
plt.legend()
plt.show()

# point 3
cars = pd.read_csv("mtcarsdata-4features.csv")
cars.columns = cars.columns.str.replace(" ", "")
cars = cars.to_dict(orient="records")

variables = ["weight", "mpg"]
carsSubSetlist = fromdicttolist(cars, variables)

cars1Dimwith = computeOneDimensionaWITHinterception(carsSubSetlist)
oneDimensionalGraph(variables, carsSubSetlist, cars1Dimwith[0], cars1Dimwith[1])
plt.legend()
plt.show()

# point 4
carsMultipleDimvar = ["disp", "hp", "weight"]
carsMultipleList = fromdicttolist(cars, carsMultipleDimvar)

goalLabel = ["mpg"]
carsMPG = fromdicttolist(cars, goalLabel)
for e in carsMultipleList:
    e.insert(0, 1)
carsMultDim = computeMultipleDimensional(carsMultipleList, carsMPG)
multiDimensional(carsMPG, carsMultDim)

"""TASK 2"""
print("###-----Test regression model-----###")
perc = 0.15

repetitions = 10

print(f"\tTRAINING\tTEST\t\tTRAINING\tTEST\t\tTRAINING\t\tTEST\t\t")
print(f"\t1D without\t1D without\t1D with\t\t1D with\t\tMulti-dimensional\tMulti-dimensional")
print(f"\tinterception\tinterception\tinterception\tinterception\tinterception\t\tinterception")
for i in range(repetitions):
    #point 1
    turkishpercenttraining, turkishpercenttest = divideTrainingandTestRandomly(turkish, perc)

    wtraining = computeOneDimensional(turkishpercenttraining)
    predictraining = computelinearpredict([e[0] for e in turkishpercenttraining], wtraining)                 # 1 for t (target)
    meantraining = computeMeanSquareError([e[1] for e in turkishpercenttraining], predictraining)             # 0 for x
    #print(f"TRAINING - One-dimensional problem without intercept: {meantraining}")

    predictest = computelinearpredict([e[0] for e in turkishpercenttest], wtraining)
    meantest = computeMeanSquareError([e[1] for e in turkishpercenttest], predictest)
    #print(f"TEST - One-dimensional problem without intercept: {meantest}")
 
    # point 3                                
    carsperctraining, carsperctest = divideTrainingandTestRandomly(carsSubSetlist, perc)    # 0 weight 1 mpg
    

    w1training, w0training = computeOneDimensionaWITHinterception(carsperctraining)
    carpredictraining = computelinearpredict([e[0] for e in carsperctraining], w1training, w0training)
    carmeantraining = computeMeanSquareError([e[1] for e in carsperctraining] , carpredictraining)
    #print(f"TRAINING - One-dimensional problem with intercept: {carmeantraining}")

    carpredictest = computelinearpredict([e[0] for e in carsperctest], w1training, w0training)
    carmeantest = computeMeanSquareError([e[1] for e in carsperctest] , carpredictest)
    #print(f"TEST - One-dimensional problem with intercept: {carmeantest}")
    # point 4
    carsmultraining, carsmultest,carsMPGsubtrain, carsMPGsubtest = divideTrainingandTestRandomly(carsMultipleList, perc, carsMPG)
    carsmultrainPredict= computeMultipleDimensional(carsmultraining, carsMPGsubtrain)
    carsMULTmeantraining = computeMeanSquareError(carsMPGsubtrain, [e[0] for e in carsmultrainPredict])
    #print(f"TRAINING - Multi-dimensional problem: {carsMULTmeantraining[0]}")

    wMultipleDimensionalcars = wMultipleDimensional(carsmultraining, carsMPGsubtrain)
    carsmultestPredict = computeMultipleDimensional(carsmultest, carsMPGsubtest, wMultipleDimensionalcars)
    carsMULTmeantest = computeMeanSquareError(carsMPGsubtest, [e[0] for e in carsmultestPredict])
    #print(f"TEST - Multi-dimensional problem: {carsMULTmeantest[0]}")

    print(f"REP{i}. {meantraining:.3e}\t\t{meantest:.3e}\t{round(carmeantraining,3)}\t\t{round(carmeantest, 3)}\t\t{round(carsMULTmeantraining[0], 3)}\t\t\t{round(carsMULTmeantest[0],3)}")
