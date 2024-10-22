def computeLikelihoodLaplace(dataset, alpha):
    valueCount = {}
    classes = set(dataset['Play'])  # Insieme delle classi (es. 'yes', 'no')

    # Calcola automaticamente il numero di valori distinti per ciascun attributo
    v = {variable: len(set(dataset[variable])) for variable in dataset if variable != 'Play'}

    # Conta il numero di volte che ciascun valore appare per ogni attributo e classe
    for variable in dataset:
        if variable == 'Play':
            continue  # Salta l'attributo "Play" che è la classe di output
        valueCount[variable] = {}
        for i, value in enumerate(dataset[variable]):
            class_label = dataset['Play'][i]  # Etichetta di classe per questo campione
            if value not in valueCount[variable]:
                valueCount[variable][value] = {c: 0 for c in classes}  # Inizializza a 0 per ogni classe
            valueCount[variable][value][class_label] += 1

    # Conta il numero di occorrenze per ciascuna classe
    class_counts = {c: dataset['Play'].count(c) for c in classes}

    # Applica Laplace smoothing e calcola la probabilità condizionale per ogni attributo e valore
    for variable in valueCount:
        for value in valueCount[variable]:
            for c in classes:
                # Applica Laplace smoothing: ((count + smoothing) / (total count + smoothing * num_values[variable]))
                valueCount[variable][value][c] = (valueCount[variable][value][c] + alpha) / \
                                                 (class_counts[c] + alpha * v[variable])

    return valueCount