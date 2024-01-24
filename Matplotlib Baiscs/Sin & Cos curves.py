#;==========================================
#; Title:  Sinx and Cosx curves
#; Author: @AyemunHossain
#;==========================================

import matplotlib.pyplot as plt
import numpy as np
import math


x = np.arange(0,math.pi*2,0.05)
s = np.sin(x)
c = np.cos(x)

plt.plot(x,s,label='Sin x/y')
plt.plot(x,c,label='Cos x/y')

plt.legend()
plt.title("Trigonometric wave")
plt.xlabel('Angle')
plt.ylabel('Sinx & Cosx')

plt.show()