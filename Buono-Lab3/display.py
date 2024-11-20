import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def confusionMatrix(predictions, targetTest):
    classes = set(targetTest)
    completeConfusionMatrix = {}
    for c in classes:
        confusion = {"True Positive": 0, "True Negative": 0, "False Positive": 0, "False Negative": 0}
        for e in range(len(predictions)):
            if targetTest[e] == predictions[e] and targetTest[e] == c: confusion["True Positive"] += 1
            elif targetTest[e] != c and predictions[e] != c: confusion["True Negative"] += 1
            elif targetTest[e] == c and predictions[e] != c: confusion["False Negative"] += 1
            else: confusion["False Positive"] += 1
        completeConfusionMatrix[c] = confusion
    return completeConfusionMatrix
        #plotConfusionMatrix(confusion)
        #quality = qualityIdx(confusion)
        #print(f"\nClass {c}")
        #plotQuality(quality)

        

"""def plotConfusionMatrix(matrix):
    conf_matrix = np.array([
        [matrix["True Positive"], matrix["False Positive"]],
        [matrix["False Negative"], matrix["True Negative"]]
    ])

    labels = [key for key in matrix if "Positive" in key]
    ticks = [key for key in matrix if "Negative" in key]

    fig, ax = plt.subplots(figsize=(6, 6))
    cax = ax.matshow(conf_matrix, cmap="Blues")

    fig.colorbar(cax)

    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(labels, rotation=0, ha="center")
    ax.set_yticklabels(ticks, rotation = 90, ha="right")

    for i in range(2):
        for j in range(2):
            ax.text(j, i, str(conf_matrix[i, j]), va='center', ha='center', color="black", fontsize=12)

    plt.title("Confusion Matrix", pad=20)
    #plt.xlabel("Predicted Conditions")
    #plt.ylabel("Actual Conditions")"""
def plotConfusionMatrix(matrix, ax):
    conf_matrix = np.array([
        [matrix["True Positive"], matrix["False Positive"]],
        [matrix["False Negative"], matrix["True Negative"]]
    ])

    labels = ["True Pos", "False Pos"]
    ticks = ["False Neg", "True Neg"]

    # Plot the confusion matrix on the provided `ax`
    cax = ax.matshow(conf_matrix, cmap="Blues")

    # Add values inside the matrix with reduced font size
    for i in range(2):
        for j in range(2):
            ax.text(j, i, str(conf_matrix[i, j]), va='center', ha='center', color="black", fontsize=8)

    # Customize the axes with reduced font size
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(labels, rotation=0, ha="center", fontsize=8)
    ax.set_yticklabels(ticks, rotation=90, ha="right", fontsize=8)

    

    # Add a colorbar to the parent figure
    if hasattr(ax, 'cax'):
        ax.figure.colorbar(cax, ax=ax, fraction=0.046, pad=0.04)


def qualityIdx(confusionMatrix):
    accuracy = (confusionMatrix["True Positive"] + confusionMatrix["True Negative"])/ sum(confusionMatrix[key] for key in confusionMatrix)
    precision = confusionMatrix["True Positive"] / (confusionMatrix["True Positive"] + confusionMatrix["False Positive"])
    recall = confusionMatrix["True Positive"] / (confusionMatrix["True Positive"] + confusionMatrix["False Negative"])
    F1score = 2 *((precision * recall)/(precision + recall))

    return {"accuracy": accuracy, "precision": precision, "recall": recall, "F1 score": F1score}

def plotQuality(quality):
    for key in quality: 
        quality[key] = round(quality[key], 3) 
    
    table = pd.DataFrame.from_dict(quality, orient="index", columns=["Value"])
    print(table)


def plotMultipleConfusionMatrices(matrices, clas):
    # Create a 3x3 grid of subplots
    
    fig, axes = plt.subplots(3, 3, figsize=(10, 10))  # Reduced figure size for compactness
    fig.suptitle(f"Confusion Matrices of {clas} class", fontsize=14, y=0.93)

    # Plot each confusion matrix in the corresponding subplot
    for i, ax in enumerate(axes.flat):
        if i < len(matrices):
            plotConfusionMatrix(matrices[i], ax)
        else:
            # Hide unused subplots
            ax.axis('off')

    # Adjust spacing to bring plots closer together
    plt.subplots_adjust(wspace=0.08, hspace=0.3)  # Reduce horizontal and vertical spacing
    
    # Show the figure
    plt.show()

