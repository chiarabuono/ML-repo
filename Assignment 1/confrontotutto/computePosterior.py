def computePosterior(database, likelihood, prior): 
    post = {c: [] for c in prior}
    predictions = []  
    
    for i in range(len(database[next(iter(database))])): 
        prob = {} 
        
        for key in likelihood: 
            current_value = database[key][i]  # Ottieni il valore corrente della variabile
            # Controlla se il valore è presente in likelihood
            if current_value in likelihood[key]:  
                for c in likelihood[key][current_value]:  
                    if c not in prob: 
                        prob[c] = likelihood[key][current_value][c]
                    else: 
                        prob[c] *= likelihood[key][current_value][c]

        # Calcola la probabilità a posteriori
        for c in prior:  # Assicurati di ciclare su tutte le classi nel prior
            if c in prob:  # Verifica se la classe è presente in prob
                post[c].append(prob[c] * prior[c])
            else:
                post[c].append(0)  # Se la classe non è presente, aggiungi 0

        # Prevedi la classe massima
        max_class = max(prob, key=prob.get) if prob else None
        predictions.append(max_class)
    
    return post, predictions
