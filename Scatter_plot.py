#;=================================================
#; Title:  Scater Plot 
#; Author: @AyemunHossain
#;=================================================

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])

x = [1,2,3,4,5,6,7,8,9]
y = [5,4,6,1,9,2,5,8,10]

ax.scatter(x,y,label='scatter plot',color = 'r',marker='*',s=50)
ax.set_xlabel("X label")
ax.set_ylabel("Y label")
ax.legend()


plt.show()