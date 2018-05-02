import matplotlib.pyplot as plt
from collections import OrderedDict
import statsmodels.api as sm
import numpy as np
import pandas as pd
from scipy.stats import norm

productive_min = pd.DataFrame.from_csv("../csv/productive_min.csv", index_col="date")
steps = pd.DataFrame.from_csv("../csv/steps_daily.csv", index_col="date")
anxiety = pd.DataFrame.from_csv("../csv/anxiety.csv", index_col="date")

x = steps["value"]
y = productive_min["value"]
z = anxiety["value"]

#pearR = np.corrcoef(x,y)[1,0]

#w = np.poly1d(np.polyfit(x, y, 4))

# Fit a normal distribution
mu = 8000
sigma = 3000
x_axis = np.arange(min(x), max(x), 1000)
s = max(y)

# Label the plot
fig = plt.figure(1)
plt.title("Minutes of productivity vs. km walked")
plt.xlabel("kilometers walked")
plt.ylabel("Minutes spent on productive tasks on computer")

# Plot the data
plt.scatter(x, y)
#plt.plot(x, w(x), "b")

# Plot the normal distribution
# plt.plot(x_axis, norm.pdf([x_axis,mu,sigma], scale=s))

# Add a legend, save, and close
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), loc=4)
plt.savefig("../images/productivity_min_vs_km_walked.png")
plt.show()
plt.close()

# Label the plot
fig = plt.figure(1)
plt.title("Minutes of productivity vs. km walked")
plt.xlabel("kilometers walked")
plt.ylabel("Minutes spent on productive tasks on computer")

# Plot the data
# Add red dots for days with anxiety tagged, blue dots otherwise
for index, value in enumerate(x):
    if z.iloc[index] == 1:
        plt.scatter(value, y.iloc[index], c= "r", label="Anxiety tagged")
    else:
        plt.scatter(value, y.iloc[index], c="b", label="Anxiety not tagged")

# Plot the normal distribution
# plt.plot(x, w(x), "b")
# plt.plot(x_axis, norm.pdf([x_axis,mu,sigma], scale=s))

# Add a legend, save, and close
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), loc=4)
plt.savefig("../images/productivity_min_vs_km_walked_anxiety.png")
plt.show()
plt.close()

