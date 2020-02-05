#;===============================
#; Title:  Share X Axis part 2
#; Author: @AyemunHossain
#;===============================


import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import math
x = np.arange(0,math.pi*2,0.05)
y = np.sin(x)
z = np.sinh(x)

fig = plt.figure()
a1=fig.add_axes([0.1,0.09,0.8,0.8])
a1.plot(x,y)
a2 = a1.twinx()
a2.plot(x,z)
plt.tight_layout()
fig.legend(labels=("X","Y"),loc="upper left")
plt.show()
