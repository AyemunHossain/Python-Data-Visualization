import matplotlib as mpl
import matplotlib.pyplot as plt



fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])

hours=[9,2,8,5]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','g']

ax.pie(hours,
       labels=activities,
       colors=cols,
       startangle=70,
       explode=(0,0,0.1,0),
       autopct='%.1f%%'
       )

plt.show()