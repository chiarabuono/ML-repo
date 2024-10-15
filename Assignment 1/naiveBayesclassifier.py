def compute_prior(database):
    """
    The database is the class
    """
    classes = set(database)
    class_counts = {}
    for c in classes:
        class_counts[c] = 0
        for variable in database:
            if variable == c:
                class_counts[c] += 1
        class_counts[c] /= len(database)
    return class_counts

def compute_likelihood(database):
    value_counts = {}
    for variable in database:
        if variable == next(reversed(database)):
            continue
        value_counts[variable] = {}
        for value in database[variable]:
            if value not in value_counts[variable]:
                value_counts[variable][value] = 1
            else:
                value_counts[variable][value] += 1

        total_counts = sum(value_counts[variable].values())
        for value in value_counts[variable]:
            value_counts[variable][value] /= total_counts
    return value_counts


def naiveBayesclassifier():
    # check that test set and training set has the same amount of classes

    # Check that no entry in any of the two data sets is <1

    # Train a Naive Bayes classifier on the training set (first input argument), using its last column as the target

    # Classify the test set according to the inferred rule, and return the classification obtained

    # If the test set has a column number d+1, use this as a target, compute and return the error rate obtained (number of errors / m)

    pass