import numpy as np
from matplotlib import pyplot as plt

n = int(input())
x, y, r = [list(z) for z in zip(*[[int(a) for a in input().split()] for _ in range(n)])]

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim([0, 1000])
ax.set_ylim([0, 1000])
ax.scatter(x, y)
for i in range(n):
    cir = plt.Circle((x[i], y[i]), r[i], color='r',fill=False)
    ax.add_patch(cir)
plt.show()