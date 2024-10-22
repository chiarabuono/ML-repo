from load import load_database, divide_set_training
from naiveBayesclassifier import compute_prior, compute_likelihood, compute_posterior, compute_accuracy, computePosterior
from display import display, old_display, display_comparison
from Laplacesmoothing import laplaceLikelihood, compute_Llikelihood

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from LoadData import loadData
from computePrior import computePrior
from computeLikelihood import computeLikelihood
from computePosterior import computePosterior
from computeLikelihoodLaplace import computeLikelihoodLaplace

tsLength = 10

num_iterations = 10000

accuracies = []
accuraciesM = []

database = load_database("weather_data.txt")

dim_test_set = 4
iterations = num_iterations

for _ in range(iterations):

    data_dict, training_set, test_set = loadData('weather_data.txt',tsLength) 
   #divide_set_training(database, dim_test_set)   #res_test_set
    #data_dict, trainingSet, testSet= 
    # CONTROLLO TRA IL TEST SET E IL TRAINING TEST DA FARE

    prior_training = compute_prior(training_set["Play"])
    prior_test = compute_prior(test_set["Play"])

    #mio
    likelihood = compute_likelihood(training_set, prior_training)
    poster = compute_posterior(training_set, likelihood, prior_training)
    postertest, predictions = computePosterior(test_set, likelihood, prior_test)
    accuracy = compute_accuracy(predictions, test_set["Play"])
    accuracies.append(accuracy)

    #mattia
    priorTraining = computePrior(training_set['Play'])
    priorTest = computePrior(test_set['Play'])
    likelihood = computeLikelihood(training_set)
    posterioriTraining = computePosterior(training_set, likelihood, priorTraining)
    posterioriTest, prediction = computePosterior(test_set, likelihood, priorTest)

    res = 0

    for i in range(len(prediction)):  
        if test_set['Play'][i] == prediction[i]:  
            res += 1

    res /= len(prediction)

    accuraciesM.append(res)

# Usa pandas.cut per suddividere le accuratezze in bin con etichette discrete
bin_labels = [0, 0.25, 0.5, 0.75, 1.0]  # Etichette dei bin che vuoi usare
bins = pd.cut(accuracies, bins=len(bin_labels), labels=bin_labels, include_lowest=True)
binsLaplace = pd.cut(accuraciesM, bins=len(bin_labels), labels=bin_labels, include_lowest=True)

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
plt.title(f"Distribution of Accuracy over {num_iterations} iterations")
plt.xticks(index + bar_width / 2, bin_labels)  # Posiziona le etichette al centro delle barre
plt.legend()

# Mostra il grafico
plt.tight_layout()
plt.show()