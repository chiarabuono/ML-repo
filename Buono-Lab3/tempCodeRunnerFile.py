    # Print the results for the current class
    print(f"Confusion matrix {c} vs all: {conf}")
    print(f"Class {c} vs Rest")
    print(f"Error Rate: {error:.2f}")
    print(f"Predictions: {predictions}")
    print(f"Actual: {binaryTestTarget}\n")
    plotConfusionMatrix(conf,)