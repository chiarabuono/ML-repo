def computeOneDimensional(database):
    """
    database: list of 2-element lists where each element is [x, t]
    """
    num = 0
    den = 0
    for e in database:
        print(database[e])
        print(database[e][0])
        num += (database[e][0] * database[e][1])
        den += (database[e][0]**2)
    
    return num/den if den != 0 else None