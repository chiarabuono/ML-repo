#import tensorflow as tf
#from tensorflow.keras.datasets import mnist
#(train_X, train_y), (test_X, test_y) = mnist.load_data()

from sklearn.datasets import load_wine
from sklearn.preprocessing import MinMaxScaler
import numpy as np

from load import divideTrainingandTestRandomly
from knn import knnClassifier

wine = load_wine()
X, y = wine.data, wine.target

#for e in X:
#    for t in e:
#        print(t, end="\t")
#    print()

# scale between 0 and 1
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
for t in X_scaled:
    np.set_printoptions(suppress=True, precision=2)
    #print(t)


training, test, targetTraining, targetTest = divideTrainingandTestRandomly(X_scaled, 0.7, y)
error = knnClassifier(training, test, targetTraining, 5, targetTest)

