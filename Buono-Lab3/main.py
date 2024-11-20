#import tensorflow as tf
#from tensorflow.keras.datasets import mnist
#(train_X, train_y), (test_X, test_y) = mnist.load_data()

from sklearn.datasets import load_wine
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report

from load import divideTrainingandTestRandomly
from knn import knnClassifier
from display import confusionMatrix, plotMultipleConfusionMatrices

wine = load_wine()
X, y = wine.data, wine.target

#for e in X:
#    for t in e:
#        print(t, end="\t")
#    print()

#print("Shape X:", X.shape)
#print("Shape y:", y.shape)

# scale between 0 and 1
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
for t in X_scaled:
    np.set_printoptions(suppress=True, precision=2)
    #print(t)


training, test, targetTraining, targetTest = divideTrainingandTestRandomly(X_scaled, 0.7, y)
predictions, error = knnClassifier(training, test, targetTraining, 5, targetTest)
#confusionMatrix(predictions, targetTest)

#compute a confusion matrix, and then from it classification quality indexes. 


k_values = [1, 2, 3, 4, 5, 10, 20, 25, 30, 35, 40, 50]
divided_by_classes = {}
for c in set(targetTraining):
    divided_by_classes[c] = []
for k in k_values:
    if k % 3 == 0: continue
    predictions, error = knnClassifier(training, test, targetTraining, k, targetTest)
    confusion = confusionMatrix(predictions, targetTest)
    for c in set(targetTraining):
        divided_by_classes[c].append(confusion[c])

for c in divided_by_classes:
    plotMultipleConfusionMatrices(divided_by_classes[c], c)




# Provide an indication of typical value (e.g. an average, or a median) 

# and an appropriate measure of spread (e.g. a standard deviation, or an interval between two relevant percentiles). 

# Summarise these in appropriate tables. 
