#;==========================================
#; Title:  Customizing plots property part 1
#; Author: @AyemunHossain
#;==========================================

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,30)
y=x**2
plt.plot(x,y,'rs-')
plt.show()