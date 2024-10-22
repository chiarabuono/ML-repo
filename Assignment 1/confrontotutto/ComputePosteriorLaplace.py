def computePosteriorLaplace(database, likelihood, prior, smoothing): 
    post = {c: [] for c in prior}
    predictions = []  

    # Calcola num_values automaticamente: il numero di valori distinti per ciascuna variabile
    num_values = {key: len(set(database[key])) for key in database if key != 'Play'}
    
    for i in range(len(database[next(iter(database))])): 
        prob = {c: prior[c] for c in prior}  # Inizializza con il prior per ciascuna classe
        
        for key in likelihood: 
            current_value = database[key][i]  # Ottieni il valore corrente della variabile
            
            # Applica Laplace smoothing per ciascuna classe
            for c in prior:  
                if current_value in likelihood[key]:
                    # Se il valore è presente, usa la formula con Laplace smoothing
                    prob[c] *= (likelihood[key][current_value].get(c, 0) + smoothing) / (sum(likelihood[key][current_value].values()) + smoothing * num_values[key])
                else:
                    # Se il valore non è presente, utilizza solo il termine di smoothing
                    prob[c] *= smoothing / (smoothing * num_values[key])

        # Aggiungi la probabilità calcolata per ciascuna classe al dizionario post
        for c in prior:
            post[c].append(prob[c])

        # Prevedi la classe con la probabilità massima
        max_class = max(prob, key=prob.get) if prob else None
        predictions.append(max_class)
    
    return post, predictions
