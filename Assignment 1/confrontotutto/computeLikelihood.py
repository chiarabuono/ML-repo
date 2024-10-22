def computeLikelihood(dataset):

    valueCount = {}
    classes = set(dataset['Play'])  

    for variable in dataset:
        if variable == 'Play':
            continue 
        valueCount[variable] = {}
        for i, value in enumerate(dataset[variable]):
            class_label = dataset['Play'][i]  
            if value not in valueCount[variable]:
                valueCount[variable][value] = {c: 0 for c in classes}  
            valueCount[variable][value][class_label] += 1
    class_counts = {c: dataset['Play'].count(c) for c in classes}  
    
    for variable in valueCount:
        for value in valueCount[variable]:
            for c in classes:
                valueCount[variable][value][c] /= class_counts[c]

    return valueCount
