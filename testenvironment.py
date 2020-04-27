import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from datetime import datetime

df = pd.read_excel("01.xlsx")
OD = df["Lasermike O.D."]
ti = df["Time"] * 24
print(ti)

plt.plot(ti, OD)
plt.axhline(y=1.749)
plt.axhline(y=1.851)
plt.show(block=False)
plt.pause(10)
plt.close("all")













"""

date = df["Date"]
time = df["Time"]
datetime = pd.concat([date, time], axis=0)
print(datetime)
datetime = pd.concat([date, time], axis=1)
print(datetime)

pd.to_datetime(datetime)


"""