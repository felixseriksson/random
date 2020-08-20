summa = 0
for i in range(1, 1001):
    for k in [int(x) for x in str(i)]:
        summa += k
print(summa)