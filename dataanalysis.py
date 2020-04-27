import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

dataframe = pd.read_excel("01.xlsx")
df = dataframe[["Lasermike O.D.", "Inter Lumen Wall", "Lasermike Out of Round", "Balloon_Lumen_Height", "Guidewire Lumen Wall", "Time"]]

dataframe2 = pd.read_excel("02.xlsx")
df2 = dataframe2[["Lasermike O.D.", "Inter Lumen Wall", "Lasermike Out of Round", "Balloon_Lumen_Height", "Guidewire Lumen Wall", "Time"]]

dataframe3 = pd.read_excel("03.xlsx")
df3 = dataframe3[["Lasermike O.D.", "Inter Lumen Wall", "Lasermike Out of Round", "Balloon_Lumen_Height", "Guidewire Lumen Wall", "Time"]]

dataframe4 = pd.read_excel("04.xlsx")
df4 = dataframe4[["Lasermike O.D.", "Inter Lumen Wall", "Lasermike Out of Round", "Balloon_Lumen_Height", "Guidewire Lumen Wall", "Time"]]

OD = df["Lasermike O.D."]
ILW = df["Inter Lumen Wall"]
OoR = df["Lasermike Out of Round"]
BLH = df["Balloon_Lumen_Height"]
GLW = df["Guidewire Lumen Wall"]
ti = df["Time"] * 24

OD2 = df2["Lasermike O.D."]
ILW2 = df2["Inter Lumen Wall"]
OoR2 = df2["Lasermike Out of Round"]
BLH2 = df2["Balloon_Lumen_Height"]
GLW2 = df2["Guidewire Lumen Wall"]
ti2 = df2["Time"] * 24
#===========================================  data summary  ==============================================

with open("summary_of_variables.txt", "w") as f:
        f.write("91164963-01" "\n\n")
summary = df.describe()
print("A summary of the data by variable is provided:")
print("")
print(summary)
with open("summary_of_variables.txt", "a") as f:
    f.write(summary.to_string())

with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n""91164963-02" "\n\n")
summary = df2.describe()
print("A summary of the data by variable is provided:")
print("")
print(summary)
with open("summary_of_variables.txt", "a") as f:
    f.write(summary.to_string())

with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n""91164963-03" "\n\n")
summary = df3.describe()
print("A summary of the data by variable is provided:")
print("")
print(summary)
with open("summary_of_variables.txt", "a") as f:
    f.write(summary.to_string())

with open("summary_of_variables.txt", "a") as f:
    f.write("\n\n""91164963-04" "\n\n")
summary = df4.describe()
print("A summary of the data by variable is provided:")
print("")
print(summary)
with open("summary_of_variables.txt", "a") as f:
    f.write(summary.to_string())
#==========================  checking if data follows a normal distribution  ==========================
NorTestOD = (stats.shapiro(OD))
NorTestILW = (stats.shapiro(ILW))
NorTestOoR = (stats.shapiro(OoR))
NorTestBLH = (stats.shapiro(BLH))
NorTestGLW = (stats.shapiro(GLW))

NorTestOD2 = (stats.shapiro(OD2))
NorTestILW2 = (stats.shapiro(ILW2))
NorTestOoR2 = (stats.shapiro(OoR2))
NorTestBLH2 = (stats.shapiro(BLH2))
NorTestGLW2 = (stats.shapiro(GLW2))

print("==========================================================================================================")

with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "Normality Data for 91164963-01")

if (NorTestOD[1]) >= 0.05:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "OD is Normally Distributed")
    print("OD is Normally Distributed")
else:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "OD is not Normally Distributed")
    print("OD is not Normally Distributed")
print("""
""")
if (NorTestILW[1]) >= 0.05:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "Inter Lumen Wall is Normally Distributed")
    print("Inter Lumen Wall is Normally Distributed")
else:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "Inter Lumen Wall is not Normally Distributed")
    print("Inter Lumen Wall is not Normally Distributed")
print("""
""")
if (NorTestOoR[1]) >= 0.05:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "OoR is Normally Distributed")
    print("OoR is Normally Distributed")
else:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "OoR is not Normally Distributed")
    print("OoR is not Normally Distributed")
print("""
""")
if (NorTestBLH[1]) >= 0.05:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "Balloon Lumen Height is Normally Distributed")
    print("Balloon Lumen Height is Normally Distributed")
else:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "Balloon Lumen Height is not Normally Distributed")    
    print("Balloon Lumen Height is not Normally Distributed")
print("""
""")
if (NorTestGLW[1]) >= 0.05:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "Guidewire Lumen Wall is Normally Distributed" "\n\n")
    print("Guidewire Lumen Wall is Normally Distributed")
else:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "Guidewire Lumen Wall is not Normally Distributed" "\n\n")
    print("Guidewire Lumen Wall is not Normally Distributed")

with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "Normality Data for 91164963-02")

if (NorTestOD2[1]) >= 0.05:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "OD2 is Normally Distributed")
    print("OD2 is Normally Distributed")
else:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "OD2 is not Normally Distributed")
    print("OD2 is not Normally Distributed")
print("""
""")
if (NorTestILW2[1]) >= 0.05:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "Inter Lumen Wall is Normally Distributed")
    print("Inter Lumen Wall2 is Normally Distributed")
else:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "Inter Lumen Wall is not Normally Distributed")
    print("Inter Lumen Wall2 is not Normally Distributed")
print("""
""")
if (NorTestOoR2[1]) >= 0.05:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "OoR is Normally Distributed")
    print("OoR2 is Normally Distributed")
else:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "OoR is not Normally Distributed")
    print("OoR2 is not Normally Distributed")
print("""
""")
if (NorTestBLH2[1]) >= 0.05:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "Balloon Lumen Height is Normally Distributed")
    print("Balloon Lumen Height2 is Normally Distributed")
else:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "Balloon Lumen Height is not Normally Distributed")    
    print("Balloon Lumen Height2 is not Normally Distributed")
print("""
""")
if (NorTestGLW2[1]) >= 0.05:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "Guidewire Lumen Wall is Normally Distributed" "\n\n")
    print("Guidewire Lumen Wall2 is Normally Distributed")
else:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "Guidewire Lumen Wall2 is not Normally Distributed" "\n\n")
    print("Guidewire Lumen Wall is not Normally Distributed")
print("==========================================================================================================")

#================  histograms as part of univariate analysis  ================

plt.figure(figsize=(12,8))
plt.hist(OD, bins = 20, rwidth = 0.9, color = "r")
plt.title("Outside Diameter")
plt.axvline(x=1.749)
plt.axvline(x=1.851)
plt.xlabel("Measurment in mm")
plt.ylabel("Observations")
plt.savefig("Sepal_Width_Hist")
plt.show(block=False)
plt.pause(4)

plt.figure(figsize=(12,8))
plt.hist(OD, bins = 20, rwidth = 0.9, color = "r")
plt.hist(OD2, bins = 20, rwidth = 0.9, color = "g")
plt.title("Outside Diameter")
plt.axvline(x=1.749)
plt.axvline(x=1.851)
plt.xlabel("Measurment in mm")
plt.ylabel("Observations")
plt.savefig("Outside Diameter -01")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.plot(ti, OD)
plt.title("Outside Diameter -01")
plt.axhline(y=1.749)
plt.axhline(y=1.851)
plt.xlabel("Time")
plt.ylabel("Measurement in mm")
plt.savefig("Outside Diameter -01")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.plot(ti2, OD2)
plt.title("Outside Diameter -02")
plt.axhline(y=1.749)
plt.axhline(y=1.851)
plt.xlabel("Time")
plt.ylabel("Measurement in mm")
plt.savefig("Outside Diameter -02")
plt.show(block=False)
plt.pause(4)

plt.figure(figsize=(12,8))
plt.plot(ti, OD)
plt.plot(ti2, OD2)
plt.title("Outside Diameter -01, -02")
plt.axhline(y=1.749)
plt.axhline(y=1.851)
plt.xlabel("Time")
plt.ylabel("Measurement in mm")
plt.savefig("Outside Diameter -01 & -02")
plt.show(block=False)
plt.pause(4)
plt.close("all")

"""
plt.figure(figsize=(12,8))
plt.hist(OoR, bins = 20, rwidth = 0.9, color = "g")
plt.title("Out of Round")
plt.axvline(x=0.1016)
plt.xlabel("Measurment in mm")
plt.ylabel("Observations")
plt.savefig("Sepal_Length_Hist")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.hist(ILW, bins = 20, rwidth = 0.9, color = "b")
plt.title("Inter Lumen Wall")
plt.axvline(x=0.1041)
plt.axvline(x=0.1245)
plt.xlabel("Measurment in mm")
plt.ylabel("Observations")
plt.savefig("Petal_Width_Hist")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.hist(GLW, bins = 20, rwidth = 0.9, color = "y")
plt.title("Guidewire Lumen Wall")
plt.axvline(x=0.127)
plt.xlabel("Measurment in mm")
plt.ylabel("Observations")
plt.savefig("Petal_Length_Hist")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.hist(BLH, bins = 20, rwidth = 0.9, color = "pink")
plt.title("Balloon Lumen Height")
plt.axvline(x=0.4064)
plt.axvline(x=0.4572)
plt.xlabel("Measurment in mm")
plt.ylabel("Observations")
plt.savefig("Petal_Length_Hist")
plt.show(block=False)
plt.pause(4)
plt.close("all")
"""