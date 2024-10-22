def laplaceLikelihood(database, prior, alpha):
    valueCount = {}
    classes = set(prior)
    target_variable = next(reversed(database))
    total_values = len(database[target_variable])
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
                if valueCount[variable][value][c] == 0:
                    valueCount[variable][value][c] = (valueCount[variable][value][c] + alpha) / (class_counts[c] + alpha * v[variable])
                else:
                    valueCount[variable][value][c] /= (prior[c] * total_values)

    return valueCount
