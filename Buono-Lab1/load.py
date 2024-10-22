import random

def load_database(fileName):
    with open(fileName, "r") as f:
        lines = f.readlines()

    database = {}
    for line in lines:
        if "#" in line:
            header = [e.strip() for e in line.split("#")[1].split(" ") if e.strip() != ""]
            for e in header:
                if e != "":
                    database[e] = []
            continue

        values = [e.strip() for e in line.split(" ") if e.strip() != ""]
        for i, value in enumerate(values):
            if value == "TRUE": value = True
            elif value == "FALSE": value = False
            key = header[i] 
            database[key].append(value)
    
    return database

def divide_set_training(database, dimTestSet):
    dimDatabase = len(database[next(iter(database))])

    if dimTestSet > dimDatabase:
        raise ValueError("Database smaller then the chosen test set dimension")
    elif dimTestSet == dimDatabase:
        raise ValueError("No values usable for the training set")
    elif dimTestSet == 0:
        raise ValueError("No value usable for the test set")

    nTestSet = random.sample(range(dimDatabase), dimTestSet)
    testSet = {}
    trainingSet = {}

    for key in database:
        testSet[key] = [database[key][i] for i in nTestSet]
        trainingSet[key] = [database[key][i] for i in range(len(database[key])) if i not in nTestSet]

    if len(testSet) != len(trainingSet):
        raise ValueError("Different dimension of test set and training set")
    
    return testSet, trainingSet

def load_testset_missingsomedata(fileName):
    with open(fileName, "r") as f:
        lines = f.readlines()

    database = {}
    for line in lines:
        if "#" in line:
            header = [e.strip() for e in line.split("#")[1].split(" ") if e.strip() != ""]
            for e in header:
                if e != "":
                    database[e] = []
            continue

        values = [e.strip() for e in line.split(" ") if e.strip() != ""]
        if len(values) < len(header):
            values.append("N/A")
            
        for i, value in enumerate(values):
            if value == "TRUE": value = True
            elif value == "FALSE": value = False
            key = header[i] 
            database[key].append(value)
    
    return database