# över under metod

import time
start_time = time.time()

from math import exp
from math import floor

funktion = str(input("Ange funktion: "))
antal_steg = int(input("Ange antal steg: "))
lower_limit = int(input("Ange nedre integrationsgräns: "))
upper_limit = int(input("Ange övre integrationsgräns: "))

while :
    b = (upper_limit-lower_limit)/antal_steg

    a = 1
    x = lower_limit
    i1 = b * eval(funktion) 

    while a <antal_steg:
        a = a+1
        x = x+b
        i1 = i1+ (b * eval(funktion))

    a = 1 
    x = lower_limit + b
    i2 = b * eval(funktion)

    while a < antal_steg:
        a = a+1
        x = x+b
        i2 = i2 + (b * eval(funktion))

    

#ändra till värdesiffror ist för decimaler
    if differens < 0.0001:
        print("för ", antal_steg, " får vi 5 korrekta värdesiffror")
        break
    else:
        antal_steg = antal_steg + 1






print("--- %s seconds ---" % (time.time() - start_time))