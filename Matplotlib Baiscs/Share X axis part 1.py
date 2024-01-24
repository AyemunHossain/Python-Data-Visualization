#;===================================
#; Title:  Share X Axis part 1
#; Author: @AyemunHossain
#;=====================================


import matplotlib.pyplot as plt
import numpy as np
import math


x = np.arange(0,math.pi*2,0.05)
y = np.sin(x)
z = np.sinh(x)

fig,ax1=plt.subplots()
ax2=ax1.twinx()


a1, = ax1.plot(x,y,'r:',label="Sin")
a2, = ax2.plot(x,z,'g:',label="Sinh")

listOfaxes= [a1,a2]

ax1.legend(listOfaxes,[l.get_label() for l in listOfaxes])

plt.show()
