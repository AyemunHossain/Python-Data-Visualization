import matplotlib.pyplot as plt
fig = plt.figure()
a1=fig.add_axes([0.1,0.15,0.8,0.75])
import numpy as np
x = np.arange(1,10)
a1.plot(x, np.exp(x),'r')
a1.set_title('Exponential Graph')
a1.set_ylim(0,10000)
a1.set_xlim(0,10)
plt.show()

