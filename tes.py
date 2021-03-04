import numpy as numpy
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
dates = pd.date_range("20130101", periods=6)
csvshit = pd.read_csv("./property.csv")
csvshit = csvshit.cumsum()
plt.figure()
csvshit.plot()
plt.show()


