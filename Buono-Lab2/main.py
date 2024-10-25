import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("turkish-se-SP500vsMSCI.csv")

coordinates = df.columns
axisX = df[coordinates[0]].tolist()
axisY = df[coordinates[1]].tolist()

plt.scatter(axisX, axisY)
plt.show()