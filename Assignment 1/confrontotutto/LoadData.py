import random

def loadData (data,tsLength):

    with open(data, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines if line.strip()]
    columns = lines[0].split()
    data_rows = [line.split() for line in lines[1:]]
    data_dict = {col: [] for col in columns}

    for row in data_rows:
        for i, col in enumerate(columns):
            value = row[i]
            if value == 'TRUE':
                value = True
            elif value == 'FALSE':
                value = False
            data_dict[col].append(value)

    #Split data in trainingSet and testSet 

    if(tsLength > len(data_rows)):
        raise ValueError("Lenght greatest than the size of the database")
    
    trainingSetIndices = random.sample(range(len(data_rows)), tsLength)
    trainingSet = {col: [data_dict[col][i] for i in trainingSetIndices] for col in columns}
    testSetIndices = list(set(range(len(data_rows))) - set(trainingSetIndices))
    testSet = {col: [data_dict[col][i] for i in testSetIndices] for col in columns}

    return data_dict, trainingSet, testSet

# Choose the first 10 value of the dataset to test

# def loadData(data, tsLength):
#     with open(data, 'r') as file:
#         lines = file.readlines()

#     lines = [line.strip() for line in lines if line.strip()]
#     columns = lines[0].split()
#     data_rows = [line.split() for line in lines[1:]]
#     data_dict = {col: [] for col in columns}

#     for row in data_rows:
#         for i, col in enumerate(columns):
#             value = row[i]
#             if value == 'TRUE':
#                 value = True
#             elif value == 'FALSE':
#                 value = False
#             data_dict[col].append(value)

#     # Verifica se ci sono abbastanza dati per il training e il test
#     if tsLength > len(data_rows):
#         raise ValueError("Length greater than the size of the database")
    
#     # Prendi i primi tsLength valori per il training set
#     trainingSet = {col: data_dict[col][:tsLength] for col in columns}
    
#     # Prendi gli ultimi 4 valori per il test set
#     testSet = {col: data_dict[col][-4:] for col in columns}

#     return data_dict, trainingSet, testSet
