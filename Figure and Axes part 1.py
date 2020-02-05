#;==========================================
#; Title:  Figure and Axes part  
#; Author: @AyemunHossain
#;==========================================

import matplotlib.pyplot as plt
import numpy as np
import math


x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)

fig = plt.figure(figsize=(5,5))
ax=fig.add_axes([0.1,0.15,0.8,0.75])

ax.set_title("sine wave")
ax.set_xlabel("Angle")
ax.set_ylabel("Sine")

ax.plot(x,y)

plt.show()
