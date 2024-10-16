import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def old_display(accuracies, num_iterations):
    bin_labels = [0, 0.25, 0.5, 0.75, 1.0]  # Etichette dei bin che vuoi usare
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

def chat_display(valori):
    frequenze = Counter(valori)
    valori_possibili = [0, 0.25, 0.5, 0.75, 1]
    
    # Lista di frequenze ordinate in base ai valori possibili
    conteggi = [frequenze[valore] for valore in valori_possibili]

    # Creazione del diagramma a barre
    plt.figure(figsize=(8, 5))
    plt.bar(valori_possibili, conteggi, color='skyblue', width=0.1)

    # Aggiunta di etichette agli assi
    plt.xlabel('Valori')
    plt.ylabel('Frequenza')
    plt.title('Frequenza dei Valori')
    plt.xticks(valori_possibili)

    # Visualizzazione del grafico
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