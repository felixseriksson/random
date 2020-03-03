import time
start_time = time.time()

from math import exp

funktion = str(input("Ange funktion: "))
antal_steg = int(input("Ange antal steg: "))
lower_limit = int(input("Ange nedre integrationsgräns: "))
upper_limit = int(input("Ange övre integrationsgräns: "))

b = ((upper_limit-lower_limit)/antal_steg)

a = 0
x = lower_limit
integral = 0
while a < antal_steg:
    a = a + 1
    h1 = eval(funktion)
    rektangel = b * h1
    x = x + b
    h2 = eval(funktion)
    htriangel = h2-h1
    triangel = (htriangel * b)/2
    integral = integral + rektangel + triangel

print("Integralen är: ",integral)

print("--- %s seconds ---" % (time.time() - start_time))