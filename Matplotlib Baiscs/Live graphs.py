#;====================================
#; Title:  Live Graphs
#; Author: @AyemunHossain
#;====================================



#.................. >>>importing live data from file<<<.............#
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from  matplotlib import style


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

def animate(i):
    file = open('sample_data.txt','r')      # Run this file and open sample_data.txt and enter any data in 
    data = file.read()                      # respected formate and then click save and see the magic 
    xa=[]
    ya=[]

    linedata=data.split('\n')

    for line in linedata:
        x,y = line.split(',')
        xa.append(int(x))
        ya.append(int(y))

    ax.clear()
    ax.plot(xa,ya)

ani= animation.FuncAnimation(fig,animate,interval=1000)

plt.show()