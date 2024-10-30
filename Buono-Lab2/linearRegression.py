def createRandomSubSet():
    pass

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
    database: list of 2-element lists where each element is [mpg, weights],
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