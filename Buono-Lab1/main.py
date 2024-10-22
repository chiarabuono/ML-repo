from load import load_database, divide_set_training, load_testset_missingsomedata
from naiveBayesclassifier import compute_prior, compute_likelihood, compute_posterior, compute_errorRate
from display import display, show_errorRate, show_prediction, show_prediction_with_missingdata


### Case 1: data from the same database
database = load_database("weather_data.txt")
dim_test_set = 4
iterations = 1000

errorRates = []
errorRatesLaplace = []

for _ in range(iterations):

    test_set, training_set = divide_set_training(database, dim_test_set)

    # Naive bayes classifier
    prior_training = compute_prior(training_set["Play"])
    likelihood = compute_likelihood(training_set, prior_training)
    postertest, predictions = compute_posterior(test_set, likelihood, prior_training)
    
    errorRate = compute_errorRate(predictions, test_set["Play"])
    errorRates.append(errorRate)

display(errorRates)

### Case 2: missing "Play" data from test set ###
training_set = load_database("weather_data_training.txt")
test_set = load_testset_missingsomedata("weather_data_test.txt")

# Naive bayes classifier
prior_training = compute_prior(training_set["Play"])
likelihood = compute_likelihood(training_set, prior_training)
postertest, predictions = compute_posterior(test_set, likelihood, prior_training)

if "Play" in test_set and "N/A" not in test_set["Play"]:
    errorRate = compute_errorRate(predictions, test_set["Play"])
    show_errorRate(test_set, postertest, predictions, test_set["Play"], errorRate)
elif "Play" not in test_set:
    show_prediction(test_set, predictions)
else:
    show_prediction_with_missingdata(test_set, postertest, predictions, test_set["Play"])