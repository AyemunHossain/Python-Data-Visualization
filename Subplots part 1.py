#;==========================================
#; Title:  Matplotlib Subplots
#; Author: @AyemunHossain
#;==========================================



import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0, math.pi*2, 0.05)
y1 = np.sin(x)
y2 = np.cos(x)


fig,(ax1,ax2) = plt.subplots(nrows=2 , ncols=1)

ax1.plot(x,y1)
ax2.plot(x,y2)

plt.show()
