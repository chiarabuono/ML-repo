import numpy as np
from math import sqrt

def knnClassifier(training, test, trainingtarg, k, testarg = None):
    """
    - a set of data, as a n x d matrix, to be used as the training set
    - a corresponding column (a n x 1 matrix) of targets, i.e., class labels
    - another set of data, as a m x d matrix, to be used as the test set
    - an integer k
    - OPTIONALLY, another set of data, as a m x 1 matrix, to be used as the test set ground truth (class labels)
    """

    #Check that the number of arguments received (nargin) equals at least the number of mandatory arguments

    #Check that the number of columns of the second matrix equals the number of columns of the first matrix
    for e in range(len(test)): 
        if len(test[e]) != len(training[e]) or (len(test[e]) != len(test[e-1]) and e != 0): 
            raise ValueError("Number of argument received less that madatory arguments")
    #Check that k>0 and k<=cardinality of the training set (number of rows, above referred to as n)
    if k < 0 or k > len(training): raise ValueError(f"Cardinality out of range. Use a number between 0 and {len(training)}")
    
    #Classify the test set according to the kNN rule, and return the classification obtained
    predictions = []
    for e in range(len(test)):
        distances = []
        for tr in range(len(training)):
            distances.append([vectorNorm(test[e], training[tr]), tr])
        orded = sorted(distances, key=lambda x: x[0], reverse=False)
        neighbours = orded[:k]
        
        classes = [int(trainingtarg[n[1]]) for n in neighbours]
        prediction = max(classes, key=classes.count)
        #reality = int(testarg[e])

        predictions.append(prediction)
        #occurrence = classes.count(prediction)
    if testarg is None: return predictions

    #If the test set has the optional additional column (nargin == n.mandatory + 1), use this as a target, 
    #compute and return the error rate obtained (number of errors / m)
    error = computeErrorRate([int(t) for t in testarg], predictions)
    return error


def vectorNorm(vect1, vect2):
    if len(vect1) != len(vect2): ValueError("Not possible realize vector norm")
    distance = 0
    for e in range(len(vect1)):
        distance += (vect1[e] - vect2[e])**2
    return sqrt(distance)

def computeErrorRate(realities, predictions):
    errors = 0
    print(realities)
    print(predictions)
    for r in range(len(realities)):
        #print(realities[r], predictions[r])
        if realities[r] != predictions[r]: errors += 1
    return errors/len(realities)