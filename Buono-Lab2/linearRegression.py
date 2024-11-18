import numpy as np

def computeOneDimensional(database):
    """
    database: list of 2-element lists where each element is [x, t]
    """
    num = 0
    den = 0
    for e in database:
        num += (e[0] * e[1])
        den += (e[0]**2)
    
    return num/den if den != 0 else None

def computeOneDimensionaWITHinterception(database):
    """
    database: list of 2-element lists where each element is [weight, mpg],
            but it also works for any 2-number-pairs
    """
    if len(database) == 0: raise ValueError(f"{database} empty")
    try:
        element0 = [e[0] for e in database]
        element1 = [e[1] for e in database]
    except IndexError:
        raise ValueError("Value missing")

    mean0 = sum(element0)/len(element0)
    mean1 = sum(element1)/len(element1)

    num = 0
    den = 0
    for e in database:
        num += ((e[0]- mean0) * (e[1] - mean1))
        den += ((e[0] - mean0)**2)
    
    w1 = num/den if den != 0 else None
    w0 = mean1 - (w1 * mean0) if w1 != None else None
    
    return w1, w0

def wMultipleDimensional(matrixX, t):
    """
    returns w
    """
    matrixX = np.array(matrixX)
    return np.dot(np.dot(np.linalg.pinv(np.dot(matrixX.T, matrixX)), matrixX.T), t) 

def computeMultipleDimensional(database, target, w = None):
    """
    database: list of three elements where ["disp", "hp", "weight"]
    target: column matrix of the target
    """
    if w is None:
        w = wMultipleDimensional(database, target)
    return np.dot(database, w)

def computelinearpredict(database, angularCoefficient, offset = 0):
    predict = []
    for e in database:
        predict.append(angularCoefficient * e + offset)
    return predict

def computeMeanSquareError(expected, predicted):
    """
    expected : list
    predicted : list
    """
    error = 0
    for e in range(len(expected)):      
        error += (expected[e] - predicted[e])**2
        
    return error/len(expected)