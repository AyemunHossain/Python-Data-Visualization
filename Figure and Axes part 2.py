import matplotlib.pyplot as plt
import numpy as np
import math

plt.style.use('seaborn')
fig = plt.figure()

ax=fig.add_axes([0.1, 0.09, 0.85,  0.85])

ax.set_title("It's axes example")
ax.set_xlabel('')
ax.set_ylabel('')


y = [1, 4, 9, 16, 25,36,49, 64]
x1 = [1, 16, 30, 42,55, 68, 77,88]
x2 = [1,6,12,18,28, 40, 52, 65]


ax.plot(x1,y,'rd--')
ax.plot(x2,y,'gs-')


ax.legend(labels=('men','women'),loc='lower right')


plt.show()