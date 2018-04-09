import matplotlib.pyplot as plt
from collections import OrderedDict
import statsmodels.api as sm
import numpy as np
import pandas as pd

productive_min = pd.DataFrame.from_csv("csv/productive_min.csv", index_col="date")
steps = pd.DataFrame.from_csv("csv/steps_daily.csv", index_col="date")
anxiety = pd.DataFrame.from_csv("csv/anxiety.csv", index_col="date")

x = steps["value"]
y = productive_min["value"]
z = anxiety["value"]

#pearR = np.corrcoef(x,y)[1,0]

slope, intercept = np.polyfit(x, y, 1)
abline_values = [slope * i + intercept for i in x]

fig = plt.figure(1)
plt.title("Minutes of productivity vs. km walked")
plt.xlabel("kilometers walked")
plt.ylabel("Minutes spent on productive tasks on computer")
plt.scatter(x,y)
plt.plot(x, abline_values, "b",  label="Fit r = %6.2e"%(slope))
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), loc=4)
plt.savefig("images/productivity_min_vs_km_walked.png")
plt.show()
plt.close()

fig = plt.figure(1)
plt.title("Minutes of productivity vs. km walked")
plt.xlabel("kilometers walked")
plt.ylabel("Minutes spent on productive tasks on computer")
for index, value in enumerate(x):
    if z.iloc[index] == 1:
        plt.scatter(value, y.iloc[index], c= "r", label="Anxiety tagged")
    else:
        plt.scatter(value, y.iloc[index], c="b", label="Anxiety not tagged")
plt.plot(x, abline_values, "b",  label="Fit r = %6.2e"%(slope))
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), loc=4)
plt.savefig("images/productivity_min_vs_km_walked_anxiety.png")
plt.show()
plt.close()
