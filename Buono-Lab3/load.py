import numpy as np
def divideTrainingandTestRandomly(database, percent, sameIndexdatabase = []):
    """
    sameIndexdatabase useful in task 3 point 4 where I want to 
                return a list of corresponding element as database
    """
    dimSubset = round(percent * len(database))
    randomSubset = np.random.permutation(len(database))[:dimSubset]
    trainingset = [database[e] for e in randomSubset]
    testset = [database[e] for e in range(len(database)) if e not in randomSubset]

    if len(sameIndexdatabase) != 0:
        expectedatabasetraining = [sameIndexdatabase[e] for e in randomSubset]
        expectedatabasetest = [sameIndexdatabase[e] for e in range(len(database)) if e not in randomSubset]
        return trainingset, testset, expectedatabasetraining, expectedatabasetest
    else: return trainingset, testset
