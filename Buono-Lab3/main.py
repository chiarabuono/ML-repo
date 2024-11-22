#import tensorflow as tf
#from tensorflow.keras.datasets import mnist
#(train_X, train_y), (test_X, test_y) = mnist.load_data()

from sklearn.datasets import load_wine
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd

from load import divideTrainingandTestRandomly
from knn import knnClassifier, computeConfusionmatrix, turnToBinaryMatrix
from display import plotMultipleConfusionMatrices, plotAllQualityInOne
from quality import qualityIdx, compute_mean, compute_median, compute_stdDeviation, compute_percentile



wine = load_wine()
X, y = wine.data, wine.target


#print("Shape X:", X.shape)
#print("Shape y:", y.shape)

# scale between 0 and 1
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
for t in X_scaled:
    np.set_printoptions(suppress=True, precision=2)
    #print(t)

k_values = [1, 2, 3, 4, 5, 10, 20, 25, 30, 35, 40, 50]

accuracy = {k:{c: []  for c in set(y)} for k in k_values}
errors = {k:{c: []  for c in set(y)} for k in k_values}
precision = {k:{c: [] for c in set(y)} for k in k_values}
recall = {k:{c: [] for c in set(y)} for k in k_values}
f1score = {k:{c: [] for c in set(y)} for k in k_values}

iterations = 5

for i in range(iterations):
    training, test, targetTraining, targetTest = divideTrainingandTestRandomly(X_scaled, 0.7, y)
    classes = set(targetTraining)
    trbinarymatrix = turnToBinaryMatrix(targetTraining)
    testbinarymatrix = turnToBinaryMatrix(targetTest)

    divided_by_classes = {c:[] for c in classes}
    for k in k_values:
        for c in range(len(classes)):
            # Convert targets to binary format for current class
            binaryTrainTarget = [row[c] for row in trbinarymatrix]
            binaryTestTarget = [row[c] for row in testbinarymatrix]
            
            # Classify using kNN
            predictions, error = knnClassifier(training, test, binaryTrainTarget, k, binaryTestTarget)

            #compute a confusion matrix, and then from it classification quality indexes.
            confusion = computeConfusionmatrix(predictions, binaryTestTarget)

            indexQuality = qualityIdx(confusion)
            accuracy[k][c].append(indexQuality["accuracy"])
            precision[k][c].append(indexQuality["precision"])
            recall[k][c].append(indexQuality["recall"])
            f1score[k][c].append(indexQuality["F1 score"])
            errors[k][c].append(error)
            
            divided_by_classes[c].append(confusion)

# Summarise these in appropriate tables.
#for c in divided_by_classes:
#    plotMultipleConfusionMatrices(divided_by_classes[c], c)

# Provide an indication of typical value (e.g. an average, or a median) 
meanAccuracy = compute_mean(accuracy)
meanError = compute_mean(errors)
meanPrecision = compute_mean(precision)
meanRecall =compute_mean(recall)
meanf1score = compute_mean(f1score)

medianAccuracy = compute_median(accuracy)
medianError = compute_median(errors)
medianPrecision = compute_median(precision)
medianRecall =compute_median(recall)
medianf1score = compute_median(f1score)

# and an appropriate measure of spread (e.g. a standard deviation, or an interval between two relevant percentiles). 
stdAccuracy = compute_stdDeviation(accuracy)
stdError = compute_stdDeviation(errors)
stdPrecision = compute_stdDeviation(precision)
stdRecall = compute_stdDeviation(recall)
stdf1score = compute_stdDeviation(f1score)

percAccuracy = compute_percentile(accuracy)
percError = compute_percentile(errors)
percPrecision = compute_percentile(precision)
percRecall = compute_percentile(recall)
percf1score = compute_percentile(f1score)

#plotAllQualityInOne(meanAccuracy, meanError, meanPrecision, meanRecall, meanf1score, "Mean")
#plotAllQualityInOne(medianAccuracy, medianError, medianPrecision, medianRecall, medianf1score, "Median")
#plotAllQualityInOne(stdAccuracy, stdError, stdPrecision, stdRecall, stdf1score, "Standard deviation")
plotAllQualityInOne(percAccuracy, percError, percPrecision, percRecall, percf1score, "Range between 25th and 75th percentile")



