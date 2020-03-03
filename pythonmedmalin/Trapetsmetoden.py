#detta program approximerar integralen med trapetsmetoden
import time
start_time = time.time()

from math import exp

funktion = str(input("Ange funktion: "))
antal_steg = int(input("Ange antal steg: "))
lower_limit = int(input("Ange nedre integrationsgräns: "))
upper_limit = int(input("Ange övre integrationsgräns: "))

b = (upper_limit-lower_limit)/antal_steg

a = 1
x = lower_limit
rektangel = b * eval(funktion)
x = x + b
triangel = (b * (eval(funktion))/2)
i1 = rektangel + triangel

while a <antal_steg:
    a = a+1
    x = x+b
    rektangel = b * eval(funktion)
    x = x+b
    triangel = (b * eval(funktion))/2

    i1 = i1+ rektangel + triangel




print("Integralen är: ",i1)

print("--- %s seconds ---" % (time.time() - start_time))