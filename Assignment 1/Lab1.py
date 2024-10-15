import pandas as pd
from load import load_database, divide_set_training
from naiveBayesclassifier import compute_prior, compute_likelihood

database = load_database("weather_data.txt")

"""
for key in database:
    print(key)
    print (database[key])
"""

dim_test_set = 4
test_set, training_set, res_test_set = divide_set_training(database, dim_test_set)

class_counts = compute_prior(training_set["Play"])
value_counts = compute_likelihood(training_set)

print(value_counts)