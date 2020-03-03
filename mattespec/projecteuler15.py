#2x2 betyder 2+2 pilar varav 2 neråt och 2 åt höger
#hur många sätt att fördela 2 neråtpilar av 4 möjliga pilar?
#mxn betyder m+n pilar varav m neråt och n åt höger
#därav:
 
from math import factorial

def nchoosek():
    n = int(input("n = "))
    k = int(input("k = "))
    return factorial(n)/(factorial(k)*factorial(n-k))

x = int(nchoosek())
print(x)
#nchoosek med n = 40 och k = 20 ger svar för project euler problem 15
from mypackage import timing
#name: 
#---
#date: "2019-03-15"
#time: "18:24"
#created by Felix Eriksson
#---

