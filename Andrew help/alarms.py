import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

time = []
for i in range(0, 900100, 100):
    time.append(i)

temp_df = pd.read_csv('TemperatureLeft.csv', delimiter = ';', index_col = 0)
temp_df = temp_df.drop(['Unit'], axis=1)
temp_df = temp_df.T
temp_df['Time'] = time
time = (time[:1501])
temp_df = temp_df.set_index('Time')
temp_df.dropna
#temp_df.to_csv('LeftTemp.csv')

'''
setpoint_df = pd.read_csv('CommonInfos.csv', delimiter = ';', index_col = 0)
setpoint_df = setpoint_df[['Forming (4): Temperature (°C)', 'Machine']]
setpoint_df = setpoint_df.T
setpoint_df = setpoint_df.drop(index = 'Machine')
setpoint_df.to_csv('Setpoint.csv')
#print(setpoint_df)
'''

setpoint_df = pd.read_csv('CommonInfos.csv', delimiter = ';', index_col = 0)
setpoint_df = setpoint_df['Forming (4): Temperature (°C)']
setpoint_df = setpoint_df.T
#setpoint_df.to_csv('Setpoint.csv')
#print(setpoint_df)



#for cols in range(temp_col_start, temp_col_end):
   # print(cols)

tempdata = []
for (columnName, columnData) in temp_df.iteritems():
    tempdata.append(columnData)

#temp_col_start = temp_df[8557]
#temp_col_end = temp_df[8788]
temp_col_compare = temp_df[8777]
#temp_col_compare = tempdata

setpdata = []
for (columnName, columnData) in setpoint_df.iteritems():
   setpdata.append(columnData)

#set_col_start = setpoint_df[8557]
#set_col_end = setpoint_df[8788]
set_col_compare = setpoint_df[8777]
#set_col_compare = setpdata

#print(tempdata)
#print(setpdata[:1])

val = []
for data in tempdata:
    if data > 145:
        print(data)
    



'''
val = []
for values in temp_col_compare:
    if values >= (set_col_compare - 2):
        val.append(values)
val = (val[:1501])
val = (set_col_compare - val)
'''

'''
val = []
for values in range(temp_df[[8557], [8560]]):
    if values >= (set_col_compare - 2):
        val.append(values)
        val = (val[:1501])
        val = (set_col_compare - val)


plt.plot(time, val, linestyle = '--', label = 1)
plt.legend()
plt.show()
'''














'''
val2 = []
for values in temp_df[8558]:
    if values >= (setpoint_df[8558] - 2):
        val2.append(values)
val2 = (val2[:1501])
val2 = (setpoint_df[8558] - val2)
plt.plot(time, val2, linestyle = '--', label = 1)
plt.legend()
plt.show()


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
'''