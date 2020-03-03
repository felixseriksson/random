import time
#start_time = time.time()

from math import exp
from math import trunc
from math import log10

funktion = str(input("Ange funktion: "))
antal_steg = 0 # vid 143992 är integralerna lika till 5 värdesiffror
lower_limit = int(input("Ange nedre integrationsgräns: "))
upper_limit = int(input("Ange övre integrationsgräns: "))
övre2 = 100
undre2 = 0
k = 100000
start_time = time.time()
while övre2 - undre2 != 0:
    
    antal_steg = antal_steg + k
    b = ((upper_limit-lower_limit)/antal_steg)

    a = 0
    x = lower_limit
    undre = 0
    while a < antal_steg:
        a = a + 1
        h1 = eval(funktion)
        undre = undre + (b * h1)
        x = x + b
    a = 0
    x = lower_limit
    övre = 0
    while a < antal_steg:
        a = a + 1
        x = x + b
        h2 = eval(funktion)
        övre = övre + (b * h2)

    c = trunc(log10(undre))
    d = trunc(log10(övre))

    e = (4 - c)
    f = (4 - d)

    undreny = undre * 10**e
    övreny = övre * 10**f

    undre2 = trunc(undreny)
    övre2 = trunc(övreny)

    if övre2 - undre2 == 0 and k != 1:
        antal_steg = antal_steg - k
        k = k/10
        övre2 = 100
        undre2 = 0
    elif övre2 - undre2 == 0 and k != 1:
        break
        
        
    
print("Vid ", antal_steg, " steg är över- och underintegralen lika till 5 värdesiffror")
print("Underintegralen är ",undre)
print("Överintegralen är ",övre)





print("--- %s seconds ---" % (time.time() - start_time))