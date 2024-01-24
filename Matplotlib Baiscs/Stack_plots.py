#;=================================================
#; Title:  Matplotlib Stack Plots
#; Author: @AyemunHossain
#;=================================================


import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,10))
ax = fig.add_axes([0.1,0.1,0.8,0.8])


days = [1,2,3,4,5,6,7]

sleeping = [8,9,8,10,7,9,10]
eating = [3,2,3,2,3,3,2.5]
reading = [4,2,3,2,4,4,2.5]
playing = [3,2,3,2,2,3,2]
working = [6,9,7,8,8,5,7]


ax.stackplot(days,sleeping,eating,reading,playing,working,colors=['r','m','c','y','g'])
ax.set_xlabel('X')
ax.set_ylabel('Y')
fig.legend(labels=('Sleeping','eating','reading','playing','working'))



plt.show()