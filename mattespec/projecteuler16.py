'''
length = len(str(2**1000))
last_digit = (2**1000) % (10**(length-1))
print(last_digit)



length = len(str(287))
for n in range(1, (length+1)):
    x = (287) % (10**(n))
    print(x)
    while len(x) > 1:
'''
from mypackage import timing
#name: yeet
#---
#date: "2019-02-28"
#time: "22:37"
#created by Felix Eriksson
#---


def nthdigit(m,n):
    return (((m) // (10**n)) % 10)

length = len(str(2**1000))
digitsum = 0

for n in range(length):
    x = nthdigit(2**1000,n)
    print(x)
    digitsum += x

print(digitsum)