import time
start_time = time.time()

from math import exp
from math import pi
from math import sqrt

antal_steg = int(input("Ange antal steg: "))
lower_limit = int(input("Ange nedre integrationsgräns: "))
upper_limit = int(input("Ange övre integrationsgräns: "))
k = int(input("Ange standardavvikelsen: "))
l = int(input("Ange medelvärdet: "))
x = lower_limit
funktion = (1/(k*sqrt(2*pi))) * (exp(-((x-l)**2)/(2*k*k)))

b = ((upper_limit-lower_limit)/antal_steg)

a = 0
integral = 0
while a < antal_steg:
    a = a + 1
    h1 = (1/(k*sqrt(2*pi))) * (exp(-((x-l)**2)/(2*k*k)))
    rektangel = b * h1
    x = x + b
    #h2 = funktion
    #htriangel = h2-h1
    #triangel = (htriangel * b)/2
    integral = integral + rektangel #+ triangel

procent1 = integral * 100

procent = round(procent1, 2)
print("Sannolikheten att värdet är mellan ", lower_limit, " och ", upper_limit, " är ca. ", procent, "%.")
print(integral)

print("--- %s seconds ---" % (time.time() - start_time))