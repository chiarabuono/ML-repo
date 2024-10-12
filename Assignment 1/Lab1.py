import pandas as pd


from loadandcheck import load_database, divide_set_training

#task 1
database = load_database("weather_data.txt")

# task 2
dim_test_set = 4
test_set, training_set = divide_set_training(database, dim_test_set)




for key in database:
    variable = set(database[key])
    #print(variable)
    for value in database[key]:
        pass

