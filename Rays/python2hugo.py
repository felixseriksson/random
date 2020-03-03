'''import matplotlib as mpl
#mpl.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
'''
'''
xdata = np.linspace(0,200,100)
ydata = (np.sin(xdata))**2
#plt.plot(xdata, ydata,"ro")
plt.plot(xdata, ydata,"r-")
plt.show()
'''
'''
xdata = np.linspace(0,10,100)
ydata = np.exp(np.sin(xdata)) - 7*np.tan(xdata)
plt.plot(xdata, ydata, "r", label="nämen jisses vilken funktion titta titta")
plt.title("en jättejättefin graf")
plt.xlabel("siffror i x")
plt.ylabel("oj vilken konstig funktion")
plt.legend(loc="lower right")
plt.axis([-5, 10, -2, 100]) #typ som window i TI-miniräknare
plt.show()
'''
######################list comprehension
xdata = []
for x in range(100):
    xdata.append(x)
print(xdata)
print("\n")
xdata = [x for x in range(100)]
print(xdata)
#ta in lista från typ codejam/kattis:
# lista_med_tal = [int(x) for x in input().split]