import matplotlib.pyplot as plt

x=[1,2,3,5,6,7,8,9,10]
y=[30,65,26,24,30.20,22,31.45,26,36]

plt.plot(x,y,label='Student')
plt.xticks([1,2,3,5,6,7,8,9,10])

plt.title("Simple Polt")
plt.xlabel("Class")
plt.ylabel("Student")

plt.legend()

plt.show()

