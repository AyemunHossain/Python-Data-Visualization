#;====================================
#; Title:  Matplotlib Style Sheet part 1
#; Author: @AyemunHossain
#;====================================


import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.spines['bottom'].set_color('blue')
ax.spines['left'].set_color('red')
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_color(None)
ax.spines['top'].set_color(None)
ax.plot([1,2,3,4,5])


plt.show()
