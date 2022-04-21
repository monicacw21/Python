from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/monicawhiteside/Library/Mobile Documents/com~apple~CloudDocs/Data Sets/HappyScale+GDP2017.csv')
happyscale = df["HappyScale"]
gdp = df["GDP"]

slope, intercept, r, p, std_err = stats.linregress(happyscale, gdp)

def lineFunc(x):
    return slope * x + intercept

lineY = list(map(lineFunc, happyscale))
print(lineY)

plt.scatter(happyscale, gdp)
plt.plot(happyscale, lineY)
plt.show()

#Test function
gdpY = lineFunc(3)
print(gdpY)