'''
tar skitlång tid, fixa på nåt vis

primes = []
n = 2

def isprime(n):
    if 2**(n-1) % n == 1:
        return True
    return False

for n in range(2, 2000001):
    if isprime(n) == True:
        primes.append(n)
        print(n)

print(primes)
summan = sum(primes)
print(summan)
'''

from mypackage.fpprime import isprobablyprime

print(isprobablyprime(5))