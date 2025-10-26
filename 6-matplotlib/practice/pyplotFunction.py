import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [10,40,30,20,50,80,70,90,60,100,120,140]

plt.plot(x, y, color="yellow")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.legend("Sales")
plt.grid(color="black")
plt.ylim(1,150)
plt.xlim(1,12)
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12], ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Now', 'Dec'])

plt.show()