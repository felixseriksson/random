#numbers = []
#for n in range(2,10001):
#    numbers.append(n)
#    print(n)

#x = 1
#for x in numbers:

primes=[2]
n = 3

while len(primes) < 10001:
        for x in range (2,round(n/2)):
            if n % x == 0:
                n = n + 1
                break
        else:
            primes.append(n)
            n = n + 1
            print(n)

print(primes)