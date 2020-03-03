#detta program approximerar integralen med rektangelmetoden
import time
start_time = time.time()

from math import exp

funktion = str(input("Ange funktion: "))
antal_steg = int(input("Ange antal steg: "))
lower_limit = int(input("Ange nedre integrationsgräns: "))
upper_limit = int(input("Ange övre integrationsgräns: "))

b = (upper_limit-lower_limit)/antal_steg

a = 1
x = b/2
i1 = b * eval(funktion) 

while a <antal_steg:
    a = a+1
    x = x+b
    i1 = i1+ (b * eval(funktion))




print("Integralen är: ",i1)

print("--- %s seconds ---" % (time.time() - start_time))