import matplotlib.pyplot as plt
from collections import OrderedDict
import statsmodels.api as sm
import numpy as np
import pandas as pd
from scipy.stats import norm

# Read the data
productive_min = pd.DataFrame.from_csv("../csv/productive_min.csv", index_col="date")
mood = pd.DataFrame.from_csv("../csv/mood.csv", index_col="date")
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

# Create a dictionary of mood colors
mood_dict = {1: "#e50000", 2: "#f97306", 3: "#FFD700", 4: "#15b01a", 5 : "#0343df"}

# Plot the figure of productivity over time with days of depression and mood colors.
fig = plt.figure()
ax = fig.add_subplot(111)
for index, value in enumerate(mood["value"]):
    plt.bar(index, productive_min.iloc[index], color=mood_dict[int(mood.iloc[index])], label=int(mood.iloc[index]))
ax.set_title('Productivity over time by mood with days of depression')
ax.set_xlabel('Day')
ax.set_ylabel('Productive minutes')

# Add the labels
rects = ax.patches

for rect, label in zip(rects, depression_labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
            ha='center', va='bottom')

# Add legend
handles, labels = ax.get_legend_handles_labels()
labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0]))
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), loc=4)

plt.savefig("../images/productivity_mood_depression.png")
plt.show()
plt.close()

# Plot the figure of productivity over time with days of anxiety and mood colors.
fig = plt.figure()
ax = fig.add_subplot(111)
for index, value in enumerate(mood["value"]):
    plt.bar(index, productive_min.iloc[index], color=mood_dict[int(mood.iloc[index])], label=int(mood.iloc[index]))
ax.set_title('Productivity over time by mood with days of anxiety')
ax.set_xlabel('Day')
ax.set_ylabel('Productive minutes')

# Add the labels
rects = ax.patches
#ax.set_xticklabels(anxiety_labels)

for rect, label in zip(rects, anxiety_labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
            ha='center', va='bottom')

# Add legend
handles, labels = ax.get_legend_handles_labels()
labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0]))
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), loc=4)

plt.savefig("../images/productivity_mood_anxiety.png")
plt.show()
plt.close()

# Plot the figure of productivity over time with days of anxiety and depression without mood colors.
ax = fig.add_subplot(111)
plt.figure(figsize=(12, 8))
ax = productive_min["value"].plot(kind='bar')
ax.set_title('Productivity over time with days of depression and depression')
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
