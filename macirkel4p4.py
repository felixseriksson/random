m = 2147483647
a = 16807
b = 0
x0 = 1
lista=[0,1,2,3,4,5,6,7,8,9]

for i in range(20):
    x0 = (a*x0+b) % m
    print(lista[x0%10])