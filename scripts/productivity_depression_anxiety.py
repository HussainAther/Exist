import matplotlib.pyplot as plt
from collections import OrderedDict
import statsmodels.api as sm
import numpy as np
import pandas as pd
from scipy.stats import norm

# Read the data
productive_min = pd.DataFrame.from_csv("../csv/productive_min.csv", index_col="date")
steps = pd.DataFrame.from_csv("../csv/steps_daily.csv", index_col="date")
anxiety = pd.DataFrame.from_csv("../csv/anxiety.csv", index_col="date")
depression = pd.DataFrame.from_csv("../csv/depression.csv", index_col="date")

# Make labels for depression and anxiety that will go on the graph
anxiety_labels = []
depression_labels = []

for i in anxiety["value"]:
    if i == 1:
        anxiety_labels.append("A")
    else:
        anxiety_labels.append("")

for i in depression["value"]:
    if i == "1":
        depression_labels.append("D")
    else:
        depression_labels.append("")

# Plot the figure.
plt.figure(figsize=(12, 8))
ax = productive_min["value"].plot(kind='bar')
ax.set_title('Productivity over time with days of depression and anxiety')
ax.set_xlabel('Day')
ax.set_ylabel('Productive minutes')


# Add the labels
rects = ax.patches
ax.set_xticklabels(anxiety_labels)

for rect, label in zip(rects, depression_labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
            ha='center', va='bottom')
plt.savefig("../images/productivity_depression_anxiety.png")
plt.show()
plt.close()
