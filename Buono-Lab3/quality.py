def qualityIdx(confusionMatrix):
    accuracy = (confusionMatrix["True Positive"] + confusionMatrix["True Negative"])/ sum(confusionMatrix[key] for key in confusionMatrix)
    precision = confusionMatrix["True Positive"] / (confusionMatrix["True Positive"] + confusionMatrix["False Positive"])
    recall = confusionMatrix["True Positive"] / (confusionMatrix["True Positive"] + confusionMatrix["False Negative"])
    F1score = 2 *((precision * recall)/(precision + recall))

    return {"accuracy": accuracy, "precision": precision, "recall": recall, "F1 score": F1score}

def compute_mean(qualityIndx):
    mean = {k:{c: 0  for c in qualityIndx[k]} for k in qualityIndx}
    for k in qualityIndx:
        for c in qualityIndx[k]:
            for i in qualityIndx[k][c]:
                mean[k][c] += i
            mean[k][c] = mean[k][c]/len(qualityIndx[k][c])
    return mean

def compute_median(qualityIndx):
    median = {k: {c: 0 for c in qualityIndx[k]} for k in qualityIndx}
    for k in qualityIndx:
        for c in qualityIndx[k]:
            ordered = sorted(qualityIndx[k][c])
            n = len(ordered)
            if n % 2 == 1: median[k][c] = ordered[n // 2]
            else: median[k][c] = (ordered[n // 2] + ordered[(n // 2) - 1]) / 2   
    return median

import numpy as np
def compute_stdDeviation(qualityIndx):
    std = {k: {c: 0 for c in qualityIndx[k]} for k in qualityIndx}
    for k in qualityIndx:
        for c in qualityIndx[k]:
            std[k][c] = np.std(qualityIndx[k][c], ddof=1) 
    return std

def compute_percentile(qualityIndx):
    perc = {k: {c: 0 for c in qualityIndx[k]} for k in qualityIndx}
    for k in qualityIndx:
        for c in qualityIndx[k]:
            percentile_25 = np.percentile(qualityIndx[k][c], 25)  # 25° percentile
            percentile_75 = np.percentile(qualityIndx[k][c], 75)  # 75° percentile
            perc[k][c] = "(" + str(round(percentile_25, 3)) + ", " + str(round(percentile_75, 3)) + ")"
    return perc