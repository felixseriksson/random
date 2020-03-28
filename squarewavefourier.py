import numpy as np
from matplotlib import pyplot as plt

def gety(xvals):
    y = []
    for i in xvals:
        yval = h/2
        for n in range(1, deg+1, 2):
            yval += ((2*h)/(n*np.pi))*np.sin(n*i)
        y.append(yval)
    return y

fig = plt.figure()
ax = fig.add_subplot()

lowerx = -20
upperx = 20

lowery = -5
uppery = 15

ax.set_xlim((lowerx,upperx))
ax.set_ylim((lowery,uppery))
ax.axhline(c = "black")

x = np.linspace(lowerx, upperx, 20*(upperx-lowerx))

# set degree, odd integer
deg = 21
# set height
h = 10

y = gety(x)

plt.plot(x, y)
plt.show()

deg = 51
y = gety(x)
plt.plot(x, y)
plt.show()

deg = 101
y = gety(x)
plt.plot(x, y)
plt.show()

deg = 1001
y = gety(x)  
plt.plot(x, y)
plt.show()

deg = 5001
y = gety(x)  
plt.plot(x, y)
plt.show()

deg = 10001
y = gety(x)  
plt.plot(x, y)
plt.show()