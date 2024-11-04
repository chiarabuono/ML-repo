import numpy as np

def fromdicttolist(dict, keys):
    dictTOlist = []
    for e in dict:
        element = []
        for key in keys:
            if key in e: 
                element.append(e[key])
        dictTOlist.append(element)
    return dictTOlist

def randomSubset(database, percent):
    """
    create rondom subset of a given persentage from a list of element
    percent = decimal (like 0.5, 0.10)
    return 
            1 list if 1 database
            2 list if 2 database (one complementary to the other: training set and test set)
    """

    dimSubset = round(percent * len(database))
    randomSubset = np.random.permutation(len(database))[:dimSubset]
    databaseSubSet = [database[e] for e in randomSubset]
    
    return databaseSubSet

def divideTrainingandTestRandomly(database, percent, sameIndexdatabase = []):
    """
    sameIndexdatabase useful in task 3 point 4 where I want to 
                return a list of corresponding element as database
    """
    dimSubset = round(percent * len(database))
    randomSubset = np.random.permutation(len(database))[:dimSubset]
    trainingset = [database[e] for e in randomSubset]
    testset = [database[e] for e in range(len(database)) if e not in randomSubset]

    if sameIndexdatabase != []:
        expectedatabasetraining = [sameIndexdatabase[e] for e in randomSubset]
        expectedatabasetest = [sameIndexdatabase[e] for e in range(len(database)) if e not in randomSubset]
        return trainingset, testset, expectedatabasetraining, expectedatabasetest
    else: return trainingset, testset
