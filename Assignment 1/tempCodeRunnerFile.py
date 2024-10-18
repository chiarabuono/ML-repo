from load import load_database, divide_set_training
from naiveBayesclassifier import compute_prior, compute_likelihood, compute_posterior, compute_accuracy, computePosterior
from display import display, old_display, display_comparison
from Laplacesmoothing import laplaceLikelihood, compute_Llikelihood

database = load_database("weather_data.txt")
dim_test_set = 4
iterations = 1

accuracies = []
accuraciesLaplace = []

for _ in range(iterations):

    test_set, training_set = divide_set_training(database, dim_test_set)   #res_test_set

    # CONTROLLO TRA IL TEST SET E IL TRAINING TEST DA FARE

    prior_training = compute_prior(training_set["Play"])
    prior_test = compute_prior(test_set["Play"])

    likelihood = compute_likelihood(training_set, prior_training)
    poster = compute_posterior(training_set, likelihood, prior_training)
    postertest, predictions = computePosterior(test_set, likelihood, prior_test)
    accuracy = compute_accuracy(predictions, test_set["Play"])
    accuracies.append(accuracy)

    llikelihood = laplaceLikelihood(training_set, prior_training, 1)
    lpostertest, lpredictions = compute_posterior(test_set, llikelihood, prior_test)
    accuracyL = compute_accuracy(lpredictions, test_set["Play"])
    accuraciesLaplace.append(accuracyL)

display_comparison(accuracies, accuraciesLaplace)

print(poster)