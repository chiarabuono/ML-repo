import pandas as pd
import matplotlib.pyplot as plt

def display(errorRates):
    bin_labels = sorted(list(set(errorRates)))
    num_iterations = len(errorRates)

    bins = pd.cut(errorRates, bins=len(bin_labels), labels=bin_labels, include_lowest=True)
    bin_counts = bins.value_counts().sort_index()
    bin_percentages = (bin_counts / num_iterations) * 100

    plt.figure(figsize=(10, 6))
    plt.bar(bin_percentages.index.astype(str), bin_percentages.values, width=0.4, color='b', edgecolor='black')
    plt.xlabel('Error rate')
    plt.ylabel('Percentage of Samples (%)')
    plt.title(f"Distribution of error rate over {num_iterations} iterations")
    plt.show()

def show_errorRate(test_set, poster, predictions, real, errorRate):
    for e in range(len(predictions)):
        for key in test_set:
            if key != "Play": print(test_set[key][e], end="\t") 
        print()
        for c in poster:
            print(f"{c}: {poster[c][e]}")
        print(f"Reality: {real[e]}")
        print(f"Prediction: {predictions[e]}\n")
    print("----")
    print(f"Overall error rate {errorRate}")

def show_prediction(test_set, predictions):
    for e in range(len(predictions)):
        for key in test_set:
            if key != "Play": print(test_set[key][e], end="\t") 
        print(f"Prediction: {predictions[e]}\n")

def show_prediction_with_missingdata(test_set, poster, predictions, real):
    for e in range(len(predictions)):
        for key in test_set:
            if key != "Play": print(test_set[key][e], end="\t") 
        print()
        for c in poster:
            print(f"{c}: {poster[c][e]}")
        if real[e] != "N/A":
            print(f"Reality: {real[e]}")
        print(f"Prediction: {predictions[e]}\n")