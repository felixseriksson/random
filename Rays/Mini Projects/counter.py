from math import trunc

def frequency_checker(lista):
    counterlist = [0,0,0,0,0,0,0,0,0]
    for n in lista:
        temp = counterlist[int(n)-1] + 1
        counterlist[int(n)-1] = temp
    return counterlist

datapunkter = []

data = open("datatext.txt","r")

for line in data:
    sträng = str(line).strip("\n")
    siffra = int(sträng[:1])
    datapunkter.append(siffra)

print(datapunkter)

frekvenser = frequency_checker(datapunkter)
print(frekvenser)




