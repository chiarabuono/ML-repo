import pandas as pd
from load import load_database, divide_set_training
from naiveBayesclassifier import compute_prior, compute_likelihood, compute_posterior, compute_accuracy
from display import display, chat_display
from Laplacesmoothing import laplaceLikelihood, laplacePosterior
from pprint import *

database = load_database("weather_data.txt")
dim_test_set = 0
iterations = 1


for _ in range(iterations):

    test_set, training_set = divide_set_training(database, dim_test_set)   #res_test_set

    # CONTROLLO TRA IL TEST SET E IL TRAINING TEST DA FARE

    prior_training = compute_prior(training_set["Play"])
    #prior_test = compute_prior(test_set["Play"])

    likelihood = compute_likelihood(training_set, prior_training)

    poster = compute_posterior(training_set, likelihood, prior_training)
    #postertest, predictions = compute_posterior(test_set, likelihood, prior_test)
    #accuracy = compute_accuracy(predictions, test_set["Play"])

    pprint(likelihood)
    pprint(poster)

for _ in range(iterations):

    test_set, training_set = divide_set_training(database, dim_test_set)   #res_test_set

    # CONTROLLO TRA IL TEST SET E IL TRAINING TEST DA FARE

    prior_training = compute_prior(training_set["Play"])
    #prior_test = compute_prior(test_set["Play"])

    likelihood = laplaceLikelihood(training_set, prior_training, 1)

    poster = compute_posterior(training_set, likelihood, prior_training)
    #postertest, predictions = compute_posterior(test_set, likelihood, prior_test)
    #accuracy = compute_accuracy(predictions, test_set["Play"])
    pprint(likelihood)