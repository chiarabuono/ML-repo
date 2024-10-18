import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def old_display(accuracies):
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
    plt.xlabel('Accuracy')
    plt.ylabel('Percentage of Samples (%)')
    plt.title(f"Distribution of Accuracy over {num_iterations} iterations")
    plt.show()

def display(accuracies):
    frequency = Counter(accuracies)
    labels = [0, 0.25, 0.5, 0.75, 1]
    
    # Lista di frequenze ordinate in base ai valori possibili
    counts = [frequency[value] for value in labels]

    # Creazione del diagramma a barre
    plt.figure(figsize=(8, 5))
    plt.bar(labels, counts, color='blue', width=0.1)

    # Aggiunta di etichette agli assi
    plt.xlabel('Accuracy')
    plt.ylabel('Percentage of Samples (%)')
    plt.title('Frequency')
    plt.xticks(labels)

    # Visualizzazione del grafico
    plt.show()


def display_comparison(accuracies1, name1, accuracies2, name2):
    # Combine accuracy labels from both datasets to create common bins
    bin_labels = sorted(list(set(accuracies1 + accuracies2)))
    num_iterations1 = len(accuracies1)
    num_iterations2 = len(accuracies2)
    
    # Create bins for both sets of accuracies
    bins1 = pd.cut(accuracies1, bins=len(bin_labels), labels=bin_labels, include_lowest=True)
    bins2 = pd.cut(accuracies2, bins=len(bin_labels), labels=bin_labels, include_lowest=True)

    # Count occurrences in each bin for both datasets
    bin_counts1 = bins1.value_counts().sort_index()
    bin_counts2 = bins2.value_counts().sort_index()

    # Convert counts to percentages
    bin_percentages1 = (bin_counts1 / num_iterations1) * 100
    bin_percentages2 = (bin_counts2 / num_iterations2) * 100

    # Set the positions of the bars
    bar_width = 0.4  # Width of each bar
    indices = range(len(bin_labels))  # Indices for the bar positions
    
    # Plotting the bar chart
    plt.figure(figsize=(10, 6))
    
    # Bars for the first set of accuracies
    plt.bar([i - bar_width/2 for i in indices], bin_percentages1.values, width=bar_width, 
            color='b', label= name1, edgecolor='black')
    
    # Bars for the second set of accuracies
    plt.bar([i + bar_width/2 for i in indices], bin_percentages2.values, width=bar_width, 
            color='r', label= name2, edgecolor='black')
    
    # Labeling and title
    plt.xlabel('Accuracy')
    plt.ylabel('Percentage of Samples (%)')
    plt.title(f"Comparison of Accuracy Distribution over {num_iterations1} and {num_iterations2} iterations")
    plt.xticks(indices, bin_labels)  # Set the x-axis labels to the accuracy values
    plt.legend()
    
    # Display the plot
    plt.show()
