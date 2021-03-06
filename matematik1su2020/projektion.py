import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.grid(True)

#lower, upper axis range
lower = -15
upper = 15

ax.set_xlim((lower,upper))
ax.set_ylim((lower,upper))
ax.set_zlim((lower,upper))

ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])

xzeros = [0 for i in range(20*(upper-lower))]
yzeros = [0 for i in range(20*(upper-lower))]
zzeros = [0 for i in range(20*(upper-lower))]
xspread = np.linspace(lower, upper, 20*(upper-lower))
yspread = np.linspace(lower, upper, 20*(upper-lower))
zspread = np.linspace(lower, upper, 20*(upper-lower))

ax.plot(xspread, yzeros, zzeros, color="k")
ax.plot(xzeros, yspread, zzeros, color="k")
ax.plot(xzeros, yzeros, zspread, color="k")

a= -10
b = 10
c = 5

x1 = [0]
y1 = [0]
z1 = [0]
xdir1 = [-10]
ydir1 = [0]
zdir1 = [10]

x2 = [0, 0]
y2 = [0, 0]
z2 = [0, 0]
xdir2 = [a, (a-c)/2]
ydir2 = [b, 0]
zdir2 = [c, (c-a)/2]

x3 = [a]
y3 = [b]
z3 = [c]
xdir3 = [(a-c)/2-a]
ydir3 = [0-b]
zdir3 = [(c-a)/2-c]

#För att visa planet x-y-z=0, vänligen avkommentera rad nedan med "#"
#'''
#---

point  = np.array([0, 0, 0])
normal = np.array([1, -1, -1])

# a plane is a*x+b*y+c*z+d=0
# [a,b,c] is the normal. Thus, we have to calculate
# d and we're set
d = -point.dot(normal)

# create x,y
xx, yy = np.meshgrid(range(-15, 15), range(-15, 15))

# calculate corresponding z
z = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2]

# plot the surface
ax.plot_surface(xx, yy, z, cmap="gray", alpha=0.5)

#---
#'''


ax.quiver(x1, y1, z1, xdir1, ydir1, zdir1, length=1, arrow_length_ratio = 0.3, normalize=False)
ax.quiver(x2, y2, z2, xdir2, ydir2, zdir2, length=1, arrow_length_ratio = 0.3, normalize=False, color="red")
ax.quiver(x3, y3, z3, xdir3, ydir3, zdir3, length=1, arrow_length_ratio = 0.3, normalize=False, color="black", hatch="ooo", facecolor="none")
#för att visa den speglade vektorn, vänligen avkommentera rad nedan med "#"
#'''
ax.quiver(0, 0, 0, (((-a)/6) + (c/6)), (((2*a)/3) - ((2*c)/3)), ((a/6) - (c/6)), length=1, arrow_length_ratio = 0.3, normalize=False, color="green")
#'''
plt.show()