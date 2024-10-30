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
    dimSubset = round(percent * len(database))
    randomSubset = np.random.permutation(len(database))[:dimSubset]
    databaseSubSet = [database[e] for e in randomSubset]
    
    return databaseSubSet