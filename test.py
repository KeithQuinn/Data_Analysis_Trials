import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.animation as animation

style.use('seaborn')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    data = open('example.txt', 'r').read()
    lines = data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs, ys)
    plt.title('Test Plot')
    plt.xlabel("Measurment [mm]")
    plt.ylabel("Observations")
    
ani = animation.FuncAnimation(fig, animate, interval=1000)    
    
plt.show()