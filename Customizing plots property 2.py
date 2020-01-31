import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,30)
s = np.sin(x)
c = np.cos(x)

plt.plot(x,s,'ro:')
plt.plot(x,c,'gd--')

plt.show()