import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns


#UPN = str (input("Enter Part number: "))
#lot = str (input("Enter lot number: "))

dataframe = pd.read_excel("analyse.xlsx")
df = dataframe[["Lasermike O.D.", "Inter Lumen Wall", "Lasermike Out of Round", "Balloon_Lumen_Height", "Guidewire Lumen Wall", "Time", "Lot", "Part"]]

OD = df["Lasermike O.D."]
ILW = df["Inter Lumen Wall"]
OoR = df["Lasermike Out of Round"]
BLH = df["Balloon_Lumen_Height"]
GLW = df["Guidewire Lumen Wall"]
ti = df["Time"] * 24
lot = df["Lot"]
for lot in lot[:1]:
    (lot)
lot = str(lot)
part = df["Part"]
for part in part[:1]:
    (part)
part = str(part)

val1 = ["91164963-01", "91164963-02"]
val2 = ["91164963-03", "91164963-04"]

#===========================================  data summary  ==============================================

with open("summary_of_variables.txt", "w") as f:
    f.write("\n" "=======================================================================================================================================")
    f.write("\n\n" "Summary Data: ")
    f.write("\n\n" "Part Number: ")
    f.write(part)
    f.write("\n" "lot Number: ")
    f.write(lot)

summary = df.describe()
with open("summary_of_variables.txt", "a") as f:
    f.write("\n\n")
    f.write(summary.to_string())

#==========================  checking if data follows a normal distribution  ==========================
NorTestOD = (stats.shapiro(OD))
NorTestILW = (stats.shapiro(ILW))
NorTestOoR = (stats.shapiro(OoR))
NorTestBLH = (stats.shapiro(BLH))
NorTestGLW = (stats.shapiro(GLW))

with open("summary_of_variables.txt", "a") as f:
    f.write("\n" "==========================================================================================================")
    f.write("\n\n" "Normality Data: ")
    f.write("\n\n" "Part Number: ")
    f.write(part)
    f.write("\n" "lot Number: ")
    f.write(lot)

if (NorTestOD[1]) >= 0.05:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "OD is Normally Distributed")
else:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "OD is not Normally Distributed")
if (NorTestILW[1]) >= 0.05:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "Inter Lumen Wall is Normally Distributed")
else:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "Inter Lumen Wall is not Normally Distributed")
if (NorTestOoR[1]) >= 0.05:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "OoR is Normally Distributed")
else:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "OoR is not Normally Distributed")
if (NorTestBLH[1]) >= 0.05:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "Balloon Lumen Height is Normally Distributed")
else:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "Balloon Lumen Height is not Normally Distributed")    
if (NorTestGLW[1]) >= 0.05:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "Guidewire Lumen Wall is Normally Distributed" "\n\n")
else:
    with open("summary_of_variables.txt", "a") as f:
        f.write("\n\n" "Guidewire Lumen Wall is not Normally Distributed" "\n\n")


#================  histograms as part of univariate analysis  ================


if part in val1:
    plt.figure(figsize=(12,8))
    sns.set(style="whitegrid")
    plt.hist(OD, bins = 20, rwidth = 0.9, color = "grey", label = lot)
    plt.title(part)
    plt.legend(loc = "upper right")
    plt.axvline(x=1.749, color = "r", linewidth=2, linestyle = "dashed")
    plt.axvline(x=1.851, color = "r", linewidth=2, linestyle = "dashed")
    plt.tick_params(axis='x', colors='grey', direction='out', length=4, width=2)
    plt.xlabel("Measurment [mm]", color = "green")
    plt.ylabel("Observations", color = "green")
    plt.savefig("Histogram for OD")
    plt.show(block=False)
    plt.pause(4)
    plt.close("all")

    plt.figure(figsize=(12,8))
    plt.plot(ti, OD, color = "blue", linewidth=3, label = lot)
    plt.title(part)
    plt.legend(loc = "upper right")
    plt.axhline(y=1.749, color = "g", linewidth=2, linestyle = "dashed", label = "test")
    plt.axhline(y=1.851, color = "g", linewidth=2, linestyle = "dashed", label = "test")
    plt.tick_params(axis='x', colors='grey', direction='out', length=4, width=2)
    plt.tick_params(axis='y', colors='grey', direction='out', length=4, width=2)
    plt.xlabel("Time", color = "green")
    plt.ylabel("Measurement [mm]", color = "green")
    plt.savefig("TimeSeriesPlot for OD")
    plt.show(block=False)
    plt.pause(4)
    plt.close("all")

    plt.figure(figsize=(12,8))
    sns.set(style="whitegrid")
    sns.boxplot(y = OD, color = "g", width = 0.4)
    plt.title(part)
    plt.axhline(y=1.749, color = "orange", linewidth=2, linestyle = "dashed", label = "test")
    plt.axhline(y=1.851, color = "orange", linewidth=2, linestyle = "dashed", label = "test")
    plt.tick_params(axis='x', colors='grey', direction='out', length=4, width=2)
    plt.tick_params(axis='y', colors='grey', direction='out', length=4, width=2)
    plt.xlabel(lot)
    plt.ylabel("Measurement [mm]", color = "green")
    plt.savefig("Boxplot for OD")
    plt.show(block=False)
    plt.pause(4)
    plt.close("all")

    plt.figure(figsize=(12,8))
    plt.hist(OoR, bins = 20, rwidth = 0.9, color = "g", label = lot)
    plt.title(part)
    plt.legend(loc = "upper right")
    plt.axvline(x=0.1016, color = "g", linewidth=2, linestyle = "dashed", label = "test")
    plt.tick_params(axis='x', colors='grey', direction='out', length=4, width=2)
    plt.xlabel("Measurment [mm]", color = "green")
    plt.ylabel("Observations", color = "green")
    plt.savefig("Histogram for OoR")
    plt.show(block=False)
    plt.pause(4)
    plt.close("all")

    plt.figure(figsize=(12,8))
    plt.hist(ILW, bins = 20, rwidth = 0.9, color = "b", label = lot)
    plt.title(part)
    plt.legend(loc = "upper right")
    plt.axvline(x=0.1041, color = "g", linewidth=2, linestyle = "dashed", label = "test")
    plt.axvline(x=0.1245, color = "g", linewidth=2, linestyle = "dashed", label = "test")
    plt.tick_params(axis='x', colors='grey', direction='out', length=4, width=2)
    plt.xlabel("Measurment [mm]", color = "green")
    plt.ylabel("Observations", color = "green")
    plt.savefig("Histogram for ILW")
    plt.show(block=False)
    plt.pause(4)
    plt.close("all")

    plt.figure(figsize=(12,8))
    plt.hist(GLW, bins = 20, rwidth = 0.9, color = "y", label = lot)
    plt.title(part)
    plt.legend(loc = "upper right")
    plt.axvline(x=0.127, color = "g", linewidth=2, linestyle = "dashed", label = "test")
    plt.tick_params(axis='x', colors='grey', direction='out', length=4, width=2)
    plt.xlabel("Measurment [mm]", color = "green")
    plt.ylabel("Observations", color = "green")
    plt.savefig("Histogram for GLW")
    plt.show(block=False)
    plt.pause(4)
    plt.close("all")

    plt.figure(figsize=(12,8))
    plt.hist(BLH, bins = 20, rwidth = 0.9, color = "purple", label = lot)
    plt.title(part)
    plt.legend(loc = "upper right")
    plt.axvline(x=0.4064, color = "g", linewidth=2, linestyle = "dashed", label = "test")
    plt.axvline(x=0.4572, color = "g", linewidth=2, linestyle = "dashed", label = "test")
    plt.tick_params(axis='x', colors='grey', direction='out', length=4, width=2)
    plt.xlabel("Measurment [mm]", color = "green")
    plt.ylabel("Observations", color = "green")
    plt.savefig("Histogram for BLH")
    plt.show(block=False)
    plt.pause(4)
    plt.close("all")

elif part in val2:
    plt.figure(figsize=(12,8))
    sns.set(style="whitegrid")
    plt.hist(OD, bins = 20, rwidth = 0.9, color = "grey", label = lot)
    plt.title(part)
    plt.legend(loc = "upper right")
    plt.axvline(x=1.854, color = "r", linewidth=2, linestyle = "dashed")
    plt.axvline(x=1.956, color = "r", linewidth=2, linestyle = "dashed")
    plt.tick_params(axis='x', colors='grey', direction='out', length=4, width=2)
    plt.xlabel("Measurment [mm]", color = "green")
    plt.ylabel("Observations", color = "green")
    plt.savefig("Histogram for OD")
    plt.show(block=False)
    plt.pause(4)
    plt.close("all")

    plt.figure(figsize=(12,8))
    plt.plot(ti, OD, color = "blue", linewidth=3, label = lot)
    plt.title(part)
    plt.legend(loc = "upper right")
    plt.axhline(y=1.854, color = "g", linewidth=2, linestyle = "dashed", label = "test")
    plt.axhline(y=1.956, color = "g", linewidth=2, linestyle = "dashed", label = "test")
    plt.tick_params(axis='x', colors='grey', direction='out', length=4, width=2)
    plt.tick_params(axis='y', colors='grey', direction='out', length=4, width=2)
    plt.xlabel("Time", color = "green")
    plt.ylabel("Measurement [mm]", color = "green")
    plt.savefig("TimeSeriesPlot for OD")
    plt.show(block=False)
    plt.pause(4)
    plt.close("all")

    plt.figure(figsize=(12,8))
    sns.set(style="whitegrid")
    sns.boxplot(y = OD, color = "g", width = 0.4)
    plt.title(part)
    plt.axhline(y=1.854, color = "orange", linewidth=2, linestyle = "dashed", label = "test")
    plt.axhline(y=1.956, color = "orange", linewidth=2, linestyle = "dashed", label = "test")
    plt.tick_params(axis='x', colors='grey', direction='out', length=4, width=2)
    plt.tick_params(axis='y', colors='grey', direction='out', length=4, width=2)
    plt.xlabel(lot)
    plt.ylabel("Measurement [mm]", color = "green")
    plt.savefig("Boxplot for OD")
    plt.show(block=False)
    plt.pause(4)
    plt.close("all")

    plt.figure(figsize=(12,8))
    plt.hist(OoR, bins = 20, rwidth = 0.9, color = "g", label = lot)
    plt.title(part)
    plt.legend(loc = "upper right")
    plt.axvline(x=0.1016, color = "g", linewidth=2, linestyle = "dashed", label = "test")
    plt.tick_params(axis='x', colors='grey', direction='out', length=4, width=2)
    plt.xlabel("Measurment [mm]", color = "green")
    plt.ylabel("Observations", color = "green")
    plt.savefig("Histogram for OoR")
    plt.show(block=False)
    plt.pause(4)
    plt.close("all")

    plt.figure(figsize=(12,8))
    plt.hist(ILW, bins = 20, rwidth = 0.9, color = "b", label = lot)
    plt.title(part)
    plt.legend(loc = "upper right")
    plt.axvline(x=0.1016, color = "g", linewidth=2, linestyle = "dashed", label = "test")
    plt.axvline(x=0.132, color = "g", linewidth=2, linestyle = "dashed", label = "test")
    plt.tick_params(axis='x', colors='grey', direction='out', length=4, width=2)
    plt.xlabel("Measurment [mm]", color = "green")
    plt.ylabel("Observations", color = "green")
    plt.savefig("Histogram for ILW")
    plt.show(block=False)
    plt.pause(4)
    plt.close("all")

    plt.figure(figsize=(12,8))
    plt.hist(GLW, bins = 20, rwidth = 0.9, color = "y", label = lot)
    plt.title(part)
    plt.legend(loc = "upper right")
    plt.axvline(x=0.1524, color = "g", linewidth=2, linestyle = "dashed", label = "test")
    plt.tick_params(axis='x', colors='grey', direction='out', length=4, width=2)
    plt.xlabel("Measurment [mm]", color = "green")
    plt.ylabel("Observations", color = "green")
    plt.savefig("Histogram for GLW")
    plt.show(block=False)
    plt.pause(4)
    plt.close("all")

    plt.figure(figsize=(12,8))
    plt.hist(BLH, bins = 20, rwidth = 0.9, color = "purple", label = lot)
    plt.title(part)
    plt.legend(loc = "upper right")
    plt.axvline(x=0.4445, color = "g", linewidth=2, linestyle = "dashed", label = "test")
    plt.tick_params(axis='x', colors='grey', direction='out', length=4, width=2)
    plt.xlabel("Measurment [mm]", color = "green")
    plt.ylabel("Observations", color = "green")
    plt.savefig("Histogram for BLH")
    plt.show(block=False)
    plt.pause(4)
    plt.close("all")
else:
    print("Incorrect file selected, this part number is not an Athletis catheter shaft extrusion")