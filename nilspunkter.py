import numpy as np
from matplotlib import pyplot as plt

#xvals = []
#yvals = []
#for n in range(11):
    #xvals.append(numpy.random.uniform(0,1))
    #yvals.append(numpy.random.uniform(0,1))

vals = np.random.rand(11, 11)

plt.scatter(vals[0], vals[1], c="red")
plt.show()