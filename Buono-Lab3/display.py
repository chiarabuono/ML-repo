import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

      
def plotConfusionMatrix(matrix, ax, k):
    conf_matrix = np.array([
        [matrix["True Positive"], matrix["False Positive"]],
        [matrix["False Negative"], matrix["True Negative"]]
    ])

    labels = ["Predict pos", "Predict neg"]
    ticks = ["Actual pos", "Actual neg"]

    cax = ax.matshow(conf_matrix, cmap="Blues")

    for i in range(2):
        for j in range(2):
            ax.text(j, i, str(conf_matrix[i, j]), va="center", ha="center", color="black", fontsize=8)

    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(labels, rotation=0, ha="center", fontsize=8)
    ax.set_yticklabels(ticks, rotation=90, ha="right", fontsize=8)  
    ax.set_title(f"k = {k}")

    if hasattr(ax, "cax"):
        ax.figure.colorbar(cax, ax=ax, fraction=0.046, pad=0.04)


def plotQuality(quality):
    for key in quality: 
        quality[key] = round(quality[key], 3) 
    
    table = pd.DataFrame.from_dict(quality, orient="index", columns=["Value"])
    print(table)


def plotMultipleConfusionMatrices(matrices, clas, title, k_values):    
    fig, axes = plt.subplots(3, 3, figsize=(10, 10)) 
    
    fig.suptitle(title, fontsize=14, y=0.95)
    subtitle = f"\nPossible ties for the following values of k \n(multiples of 2 - binary knn)\n"
    for k in k_values:
        if k % 2 == 0: title += f"{k} "
    fig.text(0.5, 0.85, subtitle, fontsize=10, ha='center')
    for i, ax in enumerate(axes.flat):
        if i < len(matrices):
            plotConfusionMatrix(matrices[i], ax, k_values[i])
        else:
            ax.axis("off")

    plt.subplots_adjust(wspace=0.2, hspace=0.4, bottom=0.04, top=0.8) 
    plt.show()

def plotOneTable(error_rate, title):
    df = pd.DataFrame(list(error_rate.items()), columns=["k", "Error Rate"])
    df.set_index("k", inplace=True) 

    fig, ax = plt.subplots(figsize=(8, 5)) 
    ax.axis("tight")
    ax.axis("off")
    ax.set_title(title, fontsize=14, fontweight="bold")

    table = ax.table(cellText=df.values, colLabels=df.columns, rowLabels=df.index, cellLoc="center", loc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.auto_set_column_width(col=list(range(len(df.columns))))

    plt.show()

def plotAllQualityInOne(averageAccuracy, averageError, averagePrecision, averageRecall, averagef1score, overall_title):
    data_with_titles = {
        "Accuracy": averageAccuracy,
        "Error": averageError,
        "Precision": averagePrecision,
        "Recall": averageRecall,
        "F1 Score": averagef1score
    }

    fig, axes = plt.subplots(2, 3, figsize=(14, 6))
    axes = axes.flatten()
    fig.suptitle(overall_title, fontsize=16, fontweight="bold", y=0.98)

    for idx, (title, data) in enumerate(data_with_titles.items()):
        df = pd.DataFrame.from_dict(data, orient="index")
        df = df.round(3)
        if len(df.columns) == 4: df.columns = ["Class 0", "Class 1", "Class 2", "Classes average"]
        else: df.columns = ["Class 0", "Class 1", "Class 2"]
        df.index.name = "k"

        ax = axes[idx]
        ax.axis("tight")
        ax.axis("off")
        ax.set_title(title, fontsize=14, y=1)

        table = ax.table(cellText=df.values, colLabels=df.columns, rowLabels=df.index, cellLoc="center", loc="center")
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.auto_set_column_width(col=list(range(len(df.columns))))

    string = f"Possible ties for the following values of k \n(multiples of 2 - binary knn)\n"
    for k in df.index:
        if k % 2 == 0: string += f"{k} "
    if len(data_with_titles) < len(axes):
        warning_idx = len(data_with_titles)
        axes[warning_idx].axis("off") 
        axes[warning_idx].text(0.5, 0.5, string,
                               wrap=True, horizontalalignment="center",
                               verticalalignment="center", fontsize=10, color="black")

    for idx in range(len(data_with_titles) + 1, len(axes)):
        fig.delaxes(axes[idx])

    plt.subplots_adjust(wspace=0.4, hspace=0.2)
    plt.show()
