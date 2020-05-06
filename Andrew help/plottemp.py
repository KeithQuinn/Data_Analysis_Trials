import pandas as pd
import matplotlib.pyplot as plt

time = []
for i in range(0, 900100, 100):
    time.append(i)

temp_df = pd.read_csv('TemperatureLeft.csv', delimiter = ';', index_col = 0)
temp_df = temp_df.drop(['Unit'], axis=1)
temp_df = temp_df.T
temp_df['Time'] = time
time = (time[:1501])
temp_df = temp_df.set_index('Time')
#print(temp_df)

setpoint_df = pd.read_csv('CommonInfos.csv', delimiter = ';', index_col = 0)
setpoint_df = setpoint_df['Forming (4): Temperature (°C)']
setpoint_df = setpoint_df.T
#print(setpoint_df)


val = []
for values in temp_df[8557]:
    if values >= (setpoint_df[8557] - 2):
        val.append(values)
val = (val[:1501])
val = (setpoint_df[8557] - val)

val2 = []
for values in temp_df[8558]:
    if values >= (setpoint_df[8558] - 2):
        val2.append(values)
val2 = (val2[:1501])
val2 = (setpoint_df[8558] - val2)

val3 = []
for values in temp_df[8564]:
    if values >= (setpoint_df[8564] - 2):
        val3.append(values)
val3 = (val3[:1501])
val3 = (setpoint_df[8564] - val3)

val4 = []
for values in temp_df[8607]:
    if values >= (setpoint_df[8607] - 2):
        val4.append(values)
val4 = (val4[:1501])
val4 = (setpoint_df[8602] - val4)

plt.plot(time, val, linestyle = '--', label = 1)
plt.plot(time, val2, linestyle = '--', label = 2)
plt.plot(time, val3, linestyle = '--', label = 3)
plt.plot(time, val4, linestyle = '--', label = 4)
plt.legend()
plt.show()