import pandas as pd
import matplotlib.pyplot as plt

def display(accuracies):
    accuracies = [1 - e for e in accuracies]
    bin_labels = sorted(list(set(accuracies)))
    num_iterations = len(accuracies)

    bins = pd.cut(accuracies, bins=len(bin_labels), labels=bin_labels, include_lowest=True)

    # Conta quante accuratezze rientrano in ciascun bin
    bin_counts = bins.value_counts().sort_index()

    # Converti i conteggi in percentuale
    bin_percentages = (bin_counts / num_iterations) * 100

    # Plotting del grafico a barre
    plt.figure(figsize=(10, 6))
    plt.bar(bin_percentages.index.astype(str), bin_percentages.values, width=0.4, color='b', edgecolor='black')
    plt.xlabel('Error rate')
    plt.ylabel('Percentage of Samples (%)')
    plt.title(f"Distribution of error rate over {num_iterations} iterations")
    plt.show()

def old_display(accuracies):
    labels = [ 1- e for e in sorted(list(set(accuracies)))]
    bins = pd.cut(accuracies, bins=len(labels), labels=labels, include_lowest=True)
    num_iterations = len(accuracies)
    bin_percentages = (bins / num_iterations) * 100

    plt.figure(figsize=(8, 5))
    plt.bar(labels, bin_percentages, color='blue', width=0.1)
    plt.xlabel('Accuracy')
    plt.ylabel('Percentage of Samples (%)')
    plt.title('Frequency')
    plt.xticks(labels)
    plt.show()


def display_comparison(accuracies1, name1, accuracies2, name2):
    bin_labels = [ 1- e for e in sorted(list(set(accuracies1 + accuracies2)))]
    num_iterations1 = len(accuracies1)
    num_iterations2 = len(accuracies2)
    
    bins1 = pd.cut(accuracies1, bins=len(bin_labels), labels=bin_labels, include_lowest=True)
    bins2 = pd.cut(accuracies2, bins=len(bin_labels), labels=bin_labels, include_lowest=True)

    bin_counts1 = bins1.value_counts().sort_index()
    bin_counts2 = bins2.value_counts().sort_index()

    bin_percentages1 = (bin_counts1 / num_iterations1) * 100
    bin_percentages2 = (bin_counts2 / num_iterations2) * 100

    bar_width = 0.4  
    indices = range(len(bin_labels))
    
    plt.figure(figsize=(10, 6))
    
    plt.bar([i - bar_width/2 for i in indices], bin_percentages1.values, width=bar_width, 
            color='b', label= name1, edgecolor='black')

    plt.bar([i + bar_width/2 for i in indices], bin_percentages2.values, width=bar_width, 
            color='r', label= name2, edgecolor='black')
    
    plt.xlabel('Error rate')
    plt.ylabel('Percentage of Samples (%)')
    plt.title(f"Comparison of Error rate over {num_iterations1} iterations")
    plt.xticks(indices, bin_labels) 
    plt.legend()
    plt.show()


def show_accuracy(test_set, poster, predictions, real, accuracy):
    for e in range(len(predictions)):
        for key in test_set:
            if key != "Play": print(test_set[key][e], end="\t") 
        print()
        for c in poster:
            print(f"{c}: {poster[c][e]}")
        print(f"Reality: {real[e]}")
        print(f"Prediction: {predictions[e]}\n")
    print("----")
    print(f"Overall accuracy {accuracy}")

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
        print(f"Reality: {real[e]}")
        print(f"Prediction: {predictions[e]}\n")