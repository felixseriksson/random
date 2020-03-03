numbers = []

for n in range(1,1000):
    if n % 3 == 0:
        numbers.append(n)
    elif n % 5 == 0:
        if n % 15 != 0:
            numbers.append(n)

summan = sum(numbers)

print(summan)