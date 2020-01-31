import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0,math.pi*2,0.05)
s = np.sin(x)
c = np.cos(x)
t = np.tan(x)

plt.plot(x,s,label='Sin x/y')
plt.plot(x,c,label='Cos x/y')
plt.plot(x,t,label='Tan x/y')

plt.legend()
plt.title("Trigonometric wave")
plt.xlabel('Angle')
plt.ylabel('Sinx & Cosx & Tanx')

plt.show()
