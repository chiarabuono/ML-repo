import pandas as pd
from load import load_database, divide_set_training

database = load_database("weather_data.txt")

"""
for key in database:
    print(key)
    print (database[key])
"""

dim_test_set = 4
test_set, training_set, res_test_set = divide_set_training(database, dim_test_set)


classes = set(training_set["Play"])

class_counts = {}
for c in classes:
    class_counts[c] = 0
    for variable in training_set["Play"]:
        if variable == c:
            class_counts[c] += 1
    class_counts[c] /= len(training_set["Play"])
print(class_counts)


"""
dd = {}
for c in classes:
    for variable in training_set:
        print(variable)
        for value in training_set[variable]:
                if variable not in dd:
                     dd[variable] = 1
                else:
                     dd[variable] += 1
print(dd)

for key in database:
    variable = set(database[key])
    #print(variable)
    for value in database[key]:
        pass

"""