def fibonacci(n):
    lista = [0, 1]
    for i in range(2,int(n)+1):
        lista.append(lista[-1]+lista[-2])
    return lista[n]

print(fibonacci(int(input("f(n), n = "))))