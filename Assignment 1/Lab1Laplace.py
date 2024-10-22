from load import load_database, divide_set_training, load_testset_missingsomedata
from naiveBayesclassifier import compute_prior, compute_posterior, compute_accuracy
from display import display, show_prediction, show_accuracy, show_prediction_with_missingdata
from Laplacesmoothing import laplaceLikelihood

database = load_database("weather_data.txt")
dim_test_set = 4
iterations = 1000
alpha = 1

accuracies = []

for _ in range(iterations):

    test_set, training_set = divide_set_training(database, dim_test_set)   #res_test_set

    

    prior_training = compute_prior(training_set["Play"])
    prior_test = compute_prior(test_set["Play"])

    likelihood = laplaceLikelihood(training_set, prior_training, alpha)
    poster = compute_posterior(training_set, likelihood, prior_training)
    postertest, predictions = compute_posterior(test_set, likelihood, prior_training)
    if "Play" in test_set:
        accuracy = compute_accuracy(predictions, test_set["Play"])
        accuracies.append(accuracy)
    else:
        print(predictions)

display(accuracies)

training_set = load_database("weather_data_training.txt")
test_set = load_testset_missingsomedata("weather_data_test.txt")

prior_training = compute_prior(training_set["Play"])
likelihood = laplaceLikelihood(training_set, prior_training, alpha)
poster = compute_posterior(training_set, likelihood, prior_training)
postertest, predictions = compute_posterior(test_set, likelihood, prior_training)

if "Play" in test_set and "N/A" not in test_set["Play"]:
    accuracy = compute_accuracy(predictions, test_set["Play"])
    show_accuracy(test_set, postertest, predictions, test_set["Play"], accuracy)
elif "Play" not in test_set:
    show_prediction(test_set, predictions)
else:
    show_prediction_with_missingdata(test_set, postertest, predictions, test_set["Play"])