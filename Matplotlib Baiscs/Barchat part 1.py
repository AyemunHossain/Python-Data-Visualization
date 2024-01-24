#;==========================================
#; Title:  Barchat part 1
#; Author: @AyemunHossain
#;==========================================

import matplotlib.pyplot as plt


x=[1,2,3,5,8,9,10,11,16]
y=[1,3,5,7,9,10,11,13,15]
y1=[1,2,1,2,0.2,2,3.5,2,3]

plt.bar(x,y,label='Student',color='red')
plt.bar(x,y1,label='Money',bottom=y)

plt.xlabel('X label')
plt.ylabel('Y label')
plt.grid(axis='y')
plt.legend()

plt.show()
