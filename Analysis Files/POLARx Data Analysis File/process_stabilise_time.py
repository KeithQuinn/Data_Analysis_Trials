import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.simplefilter(action = "ignore", category = RuntimeWarning)

time = []
for i in range(0, 900100, 100):
    time.append(i)

temp_df = pd.read_csv('TemperatureLeft.csv', delimiter = ';', index_col = 0)
temp_df = temp_df.drop(['Unit'], axis=1)
temp_df = temp_df.T
temp_df['Time'] = time
temp_df = temp_df.set_index('Time')

setpoint_df = pd.read_csv('CommonInfos.csv', delimiter = ';', index_col = 0)
setpoint_df = setpoint_df['Forming (4): Temperature (°C)']
setpoint_df = setpoint_df.T

col = 8556
time = (time[:1501])
for val in range (1, 50): 
    col = col + 1       
    val = []
    for values in temp_df[col]:
            if values >= (setpoint_df[col] - 2):
                val.append(values)
    val = (val[:1501])
    val = (setpoint_df[col] - val)
    if(len(time) == (len(val))):       
        plt.plot(time, val, linestyle = '--', label = col)

plt.xlim((0, 160000))
plt.text(143750, -4.48, "End Cycle [150s]", color = 'red')
plt.axvline(x=150000, color = "r", linewidth=2, linestyle = "dashed")
plt.title('Process Stabiliation Time', color = 'grey')
plt.xlabel("Time [miliseconds]", color = "green")
plt.ylabel("Setpoint Variation [C]", color = "green")
plt.legend()
plt.legend(loc = "upper right")
plt.savefig("Settling time")
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.show(block=False)
plt.pause(10)
plt.close("all")