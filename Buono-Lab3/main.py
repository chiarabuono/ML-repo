from sklearn.datasets import load_wine
import numpy as np

from load import divideTrainingandTestRandomly
from knn import knnClassifier, computeConfusionmatrix, turnToBinaryMatrix
from display import plotMultipleConfusionMatrices, plotAllQualityInOne, plotOneTable
from quality import qualityIdx, compute_average, compute_median, compute_stdDeviation, compute_percentile

wine = load_wine()
X, y = wine.data, wine.target

# scale between 0 and 1
X_min = X.min(axis=0)
X_max = X.max(axis=0)
X_scaled = (X - X_min) / (X_max - X_min)
np.set_printoptions(suppress=True, precision=2)

k_values = [1, 2, 3, 4, 5, 10, 15, 30, 50]

# Error rate with non-binary classifier
error_rate = {k: 0 for k in k_values}
for k in k_values:
    training, test, targetTraining, targetTest = divideTrainingandTestRandomly(X_scaled, 0.7, y)
    classes = set(targetTraining)
    predictions, error = knnClassifier(training, test, targetTraining, k, targetTest)
    error_rate[k] = round(error, 3)
plotOneTable(error_rate, "Error rate with not binary KNN")

# with 10 iterations
accuracy = {k:{c: []  for c in set(y)} for k in k_values}
errors = {k:{c: []  for c in set(y)} for k in k_values}
precision = {k:{c: [] for c in set(y)} for k in k_values}
recall = {k:{c: [] for c in set(y)} for k in k_values}
f1score = {k:{c: [] for c in set(y)} for k in k_values}

iterations = 10
for i in range(iterations):
    training, test, targetTraining, targetTest = divideTrainingandTestRandomly(X_scaled, 0.7, y)
    classes = set(targetTraining)
    trbinarymatrix = turnToBinaryMatrix(targetTraining)
    testbinarymatrix = turnToBinaryMatrix(targetTest)

    divided_by_classes = {c:[] for c in classes}
    for k in k_values:
        for c in range(len(classes)):
            
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
for c in divided_by_classes:
    plotMultipleConfusionMatrices(divided_by_classes[c], c, f"Confusion Matrices of {c} class", k_values)

# Provide an indication of typical value (e.g. an average, or a median) 
averageAccuracy = compute_average(accuracy)
averageError = compute_average(errors)
averagePrecision = compute_average(precision)
averageRecall =compute_average(recall)
averagef1score = compute_average(f1score)

max = averageAccuracy[next(iter(averageAccuracy))]["Average on class"]
k_value = 0
for k in averageAccuracy:
    if averageAccuracy[k]["Average on class"] > max:
        max = averageAccuracy[k]["Average on class"]
        k_value = k
print(f"The k that best approximates is {k} with accuracy {round(max, 3)}\n")

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

plotAllQualityInOne(averageAccuracy, averageError, averagePrecision, averageRecall, averagef1score, "Average")
plotAllQualityInOne(medianAccuracy, medianError, medianPrecision, medianRecall, medianf1score, "Median")
plotAllQualityInOne(stdAccuracy, stdError, stdPrecision, stdRecall, stdf1score, "Standard deviation")
plotAllQualityInOne(percAccuracy, percError, percPrecision, percRecall, percf1score, "Range between 25th and 75th percentile")
