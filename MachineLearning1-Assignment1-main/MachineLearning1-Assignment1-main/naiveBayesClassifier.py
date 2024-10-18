import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from LoadData import loadData
from computePrior import computePrior
from computeLikelihood import computeLikelihood
from computePosterior import computePosterior
from computeLikelihoodLaplace import computeLikelihoodLaplace

tsLength = 10

num_iterations = 1000

accuracies = []
accuraciesLaplace = []

for _ in range(num_iterations):
    #Load data

    data_dict, trainingSet, testSet= loadData('weatherData.txt',tsLength)  

    #Trainingset & testset print

    # df_trainingSet = pd.DataFrame(trainingSet)
    # df_testSet = pd.DataFrame(testSet)
    # print("\nTraining Set:\n")
    # print(df_trainingSet.to_string(index=False)) 
    # print("\nTest Set:\n")
    # print(df_testSet.to_string(index=False))
    # print("\n")

    #Compute a priori probability

    priorTraining = computePrior(trainingSet['Play'])
    priorTest = computePrior(testSet['Play'])

    #Print a priori probability

    # print("Training Set a priori probability:")
    # print(priorTraining)
    # print("\nTest Set a priori probability:")
    # print(priorTest)
    # print("\n")

    #Compute likelihood 

    likelihood = computeLikelihood(trainingSet)

    #Likelihood print

    # print("Likelihood:\n")

    # for variable, values in likelihood.items():
    #     print(f"{variable}:")
    #     for value, class_counts in values.items():
    #         rounded_class_counts = {k: round(v, 3) for k, v in class_counts.items()}
    #         print(f"  {value}: {rounded_class_counts}")


    # compute a posteriori probability

    posterioriTraining = computePosterior(trainingSet, likelihood, priorTraining)

    # print("\nA posteriori probability of the trainingSet:\n")

    # print(posterioriTraining)

    posterioriTest, prediction = computePosterior(testSet, likelihood, priorTest)

    alpha = 1

    likelihoodLaplace = computeLikelihoodLaplace(trainingSet, alpha)
    posterioriTrainingLaplace, predictiontrainingLaplace = computePosterior(trainingSet, likelihoodLaplace, priorTraining)
    posterioriTestLaplace, predictionLaplace = computePosterior(testSet, likelihoodLaplace, priorTest)

    # print("LikelihoodLaplace:\n")

    # for variable, values in likelihoodLaplace.items():
    #     print(f"{variable}:")
    #     for value, class_counts in values.items():
    #         rounded_class_counts = {k: round(v, 3) for k, v in class_counts.items()}
    #         print(f"  {value}: {rounded_class_counts}")

    # print("\nA posteriori probability of the trainingSetLaplace:\n")

    # print(posterioriTrainingLaplace)

    #Compute accuracy

    res = 0

    for i in range(len(prediction)):  
        if testSet['Play'][i] == prediction[i]:  
            res += 1

    res /= len(prediction)

    accuracies.append(res)

    resLaplace = 0

    for i in range(len(predictionLaplace)):  
        if testSet['Play'][i] == predictionLaplace[i]:  
            resLaplace += 1

    resLaplace /= len(predictionLaplace)

    accuraciesLaplace.append(resLaplace)


# # Usa pandas.cut per suddividere le accuratezze in bin con etichette discrete
# bin_labels = [0, 0.25, 0.5, 0.75, 1.0]  # Etichette dei bin che vuoi usare
# bins = pd.cut(accuracies, bins=len(bin_labels), labels=bin_labels, include_lowest=True)

# # Conta quante accuratezze rientrano in ciascun bin
# bin_counts = bins.value_counts().sort_index()

# # Converti i conteggi in percentuale
# bin_percentages = (bin_counts / num_iterations) * 100

# # Plotting del grafico a barre
# plt.figure(figsize=(10, 6))
# plt.bar(bin_percentages.index.astype(str), bin_percentages.values, width=0.4, color='b', edgecolor='black')
# plt.xlabel('Accuracy')
# plt.ylabel('Percentage of Samples (%)')
# plt.title('Distribution of Accuracy over 1000 iterations')
# plt.show()


# Usa pandas.cut per suddividere le accuratezze in bin con etichette discrete
bin_labels = [0, 0.25, 0.5, 0.75, 1.0]  # Etichette dei bin che vuoi usare
bins = pd.cut(accuracies, bins=len(bin_labels), labels=bin_labels, include_lowest=True)
binsLaplace = pd.cut(accuraciesLaplace, bins=len(bin_labels), labels=bin_labels, include_lowest=True)

# Conta quante accuratezze rientrano in ciascun bin
bin_counts = bins.value_counts().sort_index()
bin_countsLaplace = binsLaplace.value_counts().sort_index()

# Converti i conteggi in percentuale
bin_percentages = (bin_counts / num_iterations) * 100
bin_percentagesLaplace = (bin_countsLaplace / num_iterations) * 100

# Plotting del grafico a barre sovrapposto
plt.figure(figsize=(10, 6))

bar_width = 0.35  # Larghezza delle barre
index = np.arange(len(bin_labels))  # Indici per l'asse x

# Grafico delle accuratezze senza Laplace
plt.bar(index, bin_percentages.values, bar_width, label='Naive Bayes Classifier', color='b', edgecolor='black')

# Grafico delle accuratezze con Laplace
plt.bar(index + bar_width, bin_percentagesLaplace.values, bar_width, label='Laplace smoothing', color='r', edgecolor='black')

# Configurazione dell'asse x
plt.xlabel('Accuracy')
plt.ylabel('Percentage of Samples (%)')
plt.title('Distribution of Accuracy over 1000 iterations')
plt.xticks(index + bar_width / 2, bin_labels)  # Posiziona le etichette al centro delle barre
plt.legend()

# Mostra il grafico
plt.tight_layout()
plt.show()

