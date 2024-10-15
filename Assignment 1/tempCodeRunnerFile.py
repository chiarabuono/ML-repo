import pandas as pd
from load import load_database, divide_set_training
from naiveBayesclassifier import compute_prior

database = load_database("weather_data.txt")

"""
for key in database:
    print(key)
    print (database[key])
"""

dim_test_set = 4
test_set, training_set, res_test_set = divide_set_training(database, dim_test_set)

class_counts = compute_prior(training_set)

value_counts = {}
for variable in training_set:
    if variable == "Play":
        continue
    for value in training_set[variable]:
        if value not in value_counts:
            value_counts[value] = 1
        else:
            value_counts[value] += 1


print(value_counts)