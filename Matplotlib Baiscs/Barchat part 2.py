#;==========================================
#; Title:  Barchat part 2
#; Author: @AyemunHossain
#;==========================================

import numpy as np
import matplotlib.pyplot as plt

N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
xt= ['G1', 'G2', 'G3', 'G4', 'G5']
ind = np.arange(N) # the x locations for the groups
width = 0.35
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.bar(xt, menMeans, width, color='r')
ax.bar(xt, womenMeans, width,bottom=menMeans, color='b')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend(labels=['Men', 'Women'])

plt.show()