def compute_prior(database):
    class_counts = {}
    total_count = len(database)
    for label in database:
        class_counts[label] = database.count(label) / total_count
    return class_counts

def compute_likelihood(database, prior):
    classes = set(prior)
    value_counts = {}
    
    target_variable = next(reversed(database))
    total_values = len(database[target_variable])
    
    for variable in database:
        if variable == target_variable:
            continue

        value_counts[variable] = {}
        
        for c in classes:
            for i, value in enumerate(database[variable]):
                if value not in value_counts[variable]:
                    value_counts[variable][value] = {}
                if c not in value_counts[variable][value]:
                    value_counts[variable][value][c] = 0
                
                if database[target_variable][i] == c:
                    value_counts[variable][value][c] += 1
            
    for variable in value_counts:
        for value in value_counts[variable]:
            for c in classes:
                value_counts[variable][value][c] /= (prior[c] * total_values)


    return value_counts

def compute_posterior(database, likelihood, prior):
    post = {c: [] for c in prior}
    predictions = []  


    for i in range(len(database[next(iter(database))])):
        prob = {}
        for key in likelihood:
            current_value = database[key][i]
            if current_value in likelihood[key]:
                for c in likelihood[key][current_value]:
                    if c not in prob:
                        prob[c] = likelihood[key][current_value][c]
                    else:
                        prob[c] *= likelihood[key][current_value][c]
        
        for key in prior:
            if key in prob:
                post[key].append(prob[key] * prior[key])
            else:
                post[key].append(0)
        
        max_class = max(prob, key=prob.get) if prob else None
        predictions.append(max_class)
                
    return post, predictions   

def compute_errorRate(prediction, real):
    errorRate = 0

    for i in range(len(prediction)):  
        if real[i] != prediction[i]:  
            errorRate += 1

    errorRate /= len(prediction)
    return errorRate