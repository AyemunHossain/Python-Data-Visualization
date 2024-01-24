#;====================================
#; Title:  Matplotlib Histogram part 3
#; Author: @AyemunHossain
#;====================================

import matplotlib.pyplot as plt
import numpy as np
import math

fig = plt.figure()

ax=fig.add_axes([0.1, 0.09, 0.85,  0.85])

ax.set_title("Men Vs Woman :))")
ax.set_xlabel('')
ax.set_ylabel('')


y = [1, 4, 9, 16, 25, 36, 40, 42]
x1 = [1, 16, 30, 42,55, 68, 77, 88]
x2 = [1,6,12,18,28, 40, 52, 65]


x_tk= [0,10,20,30,40,50,60,70,80,90,100]
y_tk = [0,5,10,15,20,25,30,35,40,45]
ax.plot(x1,y,'rd--')
ax.plot(x2,y,'gs-')


ax.legend(labels=('men','women'),loc='lower right')

ax.set_xticks(x_tk)
ax.set_yticks(y_tk)
ax.grid(True)
plt.show()
