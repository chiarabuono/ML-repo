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

def computeOneDimensionaWITHinterception():
    """
    database: list of 2-element lists where each element is [mpg, weights],
            but it also works for any 2-number-pairs
    """
    