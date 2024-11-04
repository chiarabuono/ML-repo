import matplotlib.pyplot as plt

from linearRegression import computeOneDimensionaWITHinterception, computelinearpredict, computeMeanSquareError
from display import oneDimensionalGraph


def dimensionalWithInterception(database, variables, databaseType):                 # point 3
  
    oneDwithPerc = computeOneDimensionaWITHinterception(database)
    oneDimensionalGraph(variables, database, oneDwithPerc[0], oneDwithPerc[1])
    #plt.legend()
    #plt.show()

    # ----compute mean square error ----
    predictWithInt = computelinearpredict(database[0], oneDwithPerc[0], oneDwithPerc[1])
    meanWithInt = computeMeanSquareError(database[1], predictWithInt)
    print(f"{databaseType} - One-dimensional problem with intercept: {meanWithInt}")


  