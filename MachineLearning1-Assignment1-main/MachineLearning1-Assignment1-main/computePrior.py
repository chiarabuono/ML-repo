def computePrior(dataset):
    classes = set(dataset)

    n = {}

    for c in classes:
        n[c] = 0
        for v in dataset:
            if v == c:
                n[c] +=1
        n[c] /= len(dataset)
    return n 
