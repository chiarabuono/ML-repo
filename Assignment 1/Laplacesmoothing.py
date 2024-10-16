def old_laplaceLikelihood(database, prior, a):
    classes = set(prior)
    value_counts = {}
    
    target_variable = next(reversed(database))
    total_values = len(database[target_variable])
    
    for variable in database:
        if variable == target_variable:
            continue

        value_counts[variable] = {}
        v = len(set(database[variable]))
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
                value_counts[variable][value][c] = (value_counts[variable][value][c] + a) / ((prior[c] * total_values) + a * v)

    return value_counts

def laplacePosterior(database, likelihood, prior, a):
    post = {c: [] for c in prior}
    predictions = []  

    for i in range(len(database[next(iter(database))])):
        prob = {}
        for key in likelihood:
            v = len(likelihood[key])
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
def laplaceLikelihood(database, prior, alpha):
    valueCount = {}
    classes = set(prior)
    target_variable = next(reversed(database))
    v = {variable: len(set(database[variable])) for variable in database if variable != 'Play'}

    for variable in database:
        if variable == target_variable:
            continue
        valueCount[variable] = {}
        for i, value in enumerate(database[variable]):
            class_label = database[target_variable][i] 
            if value not in valueCount[variable]:
                valueCount[variable][value] = {c: 0 for c in classes}
            valueCount[variable][value][class_label] += 1

    class_counts = {c: database[target_variable].count(c) for c in classes}

    for variable in valueCount:
        for value in valueCount[variable]:
            for c in classes:
                valueCount[variable][value][c] = (valueCount[variable][value][c] + alpha) / \
                                                 (class_counts[c] + alpha * v[variable])

    return valueCount