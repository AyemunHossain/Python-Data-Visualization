#;==========================================
#; Title:  Sinx ,Cosx and Tan curves 2
#; Author: @AyemunHossain
#;==========================================

import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0,math.pi*2,0.05)
s = np.sin(x)
c = np.cos(x)
t = np.tan(x)

fig = plt.figure()
ax1 = plt.subplot2grid((2,2),colspan=2,loc=(0,0))
ax2 = plt.subplot2grid((2,2),colspan=2,loc=(1,0),sharex=ax1)


ax1.plot(x,s,label='Sin x/y')
ax1.plot(x,c,label='Cos x/y')
ax2.plot(x,t,label='Tan x/y')

plt.title("Trigonometric wave")

ax1.set_xlabel('Angle')
ax1.set_ylabel('Sinx /Cosx')
ax1.legend()

ax2.set_xlabel('Angle')
ax2.set_ylabel('Tanx')
ax2.legend()


plt.tight_layout()
plt.show()
