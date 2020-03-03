from math import trunc
lista = []

txtfile = open("projecteuler13.txt")

for line in txtfile:
    lista.append(line)

lista2 = []

for n in lista:
    lista2.append(n.replace('\n',''))

summan = 0

for n in lista2:
    summan += int(n)

len(str(summan))

tendigits = trunc(summan/(10**(len(str(summan))-10)))

print(tendigits)