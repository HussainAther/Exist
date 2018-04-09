import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import pandas as pd

productive_min = pd.DataFrame.from_csv("csv/productive_min.csv", index_col="date")
steps = pd.DataFrame.from_csv("csv/steps_daily.csv", index_col="date")
anxiety = pd.DataFrame.from_csv("csv/anxiety.csv", index_col="date")

x = steps["value"]
y = productive_min["value"]

#pearR = np.corrcoef(x,y)[1,0]

slope, intercept = np.polyfit(x, y, 1)
abline_values = [slope * i + intercept for i in x]

fig = plt.figure(1)
plt.title("Minutes of productivity vs. km walked")
plt.xlabel("kilometers walked")
plt.ylabel("Minutes spent on productive tasks on computer")
plt.scatter(x, y)
plt.plot(x, abline_values, 'b',  label="Fit r = %6.2e"%(slope))
plt.legend(loc=4)
plt.savefig("images/productivity_min_vs_km_walked.png")
plt.close()

#x = anxiety["value"]
#y = productive_min["value"]
#
#plt.title("Minutes of productivity vs. days with anxiety tagged")
#plt.xlabel("anxiety tagged or not")
#plt.ylabel("Minutes spent on productive tasks on computer")
#plt.plot(x, label = "Anxiety")
#plt.plot(y, label = "Minute of productivity")
#plt.legend(loc=4)
#plt.show()

