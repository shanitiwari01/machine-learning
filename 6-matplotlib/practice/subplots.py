import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [10,40,30,20,50,80,70,90,60,100,120,140]

fig, ax = plt.subplots(1,2)

ax[0].plot(x,y)

ax[1].bar(x,y)

plt.tight_layout()
plt.show()