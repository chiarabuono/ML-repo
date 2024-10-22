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

def compute_Llikelihood(database, prior, num_levels, a=1):
    """
    Compute the likelihood with Laplace smoothing for each attribute given the classes.
    
    Args:
        database: Dictionary containing the dataset (attributes and target variable).
        prior: Dictionary containing the prior probabilities of each class.
        num_levels: Dictionary containing the number of possible values for each attribute.
        a: Smoothing parameter (default is 1).
    
    Returns:
        value_counts: Dictionary containing the likelihoods with Laplace smoothing.
    """
    
    classes = set(prior.keys())  # Get unique classes from the prior
    value_counts = {}  # To store the smoothed likelihoods
    
    target_variable = next(reversed(database))  # Identify the target variable (e.g., 'Play')
    total_values = len(database[target_variable])  # Total number of instances

    # Loop through each attribute in the database
    for variable in database:
        if variable == target_variable:
            continue  # Skip the target variable

        value_counts[variable] = {}

        # Get the number of possible values for the current variable
        v = num_levels[variable]

        # Initialize counts for each attribute value, for each class
        for value in set(database[variable]):  # For each possible value in the variable
            value_counts[variable][value] = {c: 0 for c in classes}

        # Count occurrences of each attribute value conditioned on the class
        for i, value in enumerate(database[variable]):
            class_label = database[target_variable][i]  # Get the corresponding class
            value_counts[variable][value][class_label] += 1

    # Apply Laplace smoothing to the counts
    for variable in value_counts:
        v = num_levels[variable]  # Number of possible values for the attribute
        for value in value_counts[variable]:
            for c in classes:
                # Calculate the smoothed probability for each class
                class_count = sum(1 for i in range(total_values) if database[target_variable][i] == c)
                value_counts[variable][value][c] = (value_counts[variable][value][c] + a) / (class_count + a * v)

    return value_counts
