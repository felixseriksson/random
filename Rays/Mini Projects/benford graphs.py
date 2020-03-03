from matplotlib import pyplot as plt
import numpy as np

def probabilityfier(lista):
    summa = 0
    counter = 0
    for element in lista:
        summa += element
    for element in lista:
        prob = float(float(element)/summa)
        lista[counter] = prob
        counter += 1
    return lista

def mse(lista1, lista2):
    summan = 0
    for n in range(len(lista1)):
        difference = float(lista1[n])-float(lista2[n])
        summan += float(difference**2)
    mse = summan / len(lista1)
    return mse

def rmse(lista1, lista2):
    summan = 0
    for n in range(len(lista1)):
        difference = float(lista1[n])-float(lista2[n])
        summan += float(difference**2)
    mse = summan / len(lista1)
    rmse = mse**(0.5)
    return rmse

def medel(lista1,lista2,lista3,lista4,lista5,lista6):
    medelvärden = []
    counter = 0
    for n in lista1:
        temp = 0
        temp += lista1[counter]
        temp += lista2[counter]
        temp += lista3[counter]
        temp += lista4[counter]
        temp += lista5[counter]
        temp += lista6[counter]
        counter += 1
        medelvärde = temp/6
        medelvärden.append(medelvärde)
    return medelvärden

def std(medelvärden,prob1a,prob2a,prob3a,prob4a,prob5a,prob6a):
    stdvs = []
    counter = 0
    for n in medelvärden:
        summa = 0
        summa += (medelvärden[counter]-prob1a[counter])**2
        summa += (medelvärden[counter]-prob2a[counter])**2
        summa += (medelvärden[counter]-prob3a[counter])**2
        summa += (medelvärden[counter]-prob4a[counter])**2
        summa += (medelvärden[counter]-prob5a[counter])**2
        summa += (medelvärden[counter]-prob6a[counter])**2
        counter += 1
        stdv = np.sqrt((summa/5))
        stdvs.append(stdv)
    return stdvs
        


digits = [1,2,3,4,5,6,7,8,9]
dataset1 = [59, 34, 29, 17, 15, 12, 13, 6, 5]
dataset2 = [61, 31, 33, 18, 13, 11, 11, 7, 5]
dataset3 = [63, 34, 27, 20, 16, 9, 10, 9, 6]
dataset4 = [64, 31, 34, 15, 16, 12, 9, 8, 5]
dataset5 = [72, 39, 35, 24, 20, 12, 10, 10, 7]
dataset6 = [76, 37, 38, 22, 18, 13, 10, 7, 8]

prob1 = probabilityfier(dataset1)
prob2 = probabilityfier(dataset2)
prob3 = probabilityfier(dataset3)
prob4 = probabilityfier(dataset4)
prob5 = probabilityfier(dataset5)
prob6 = probabilityfier(dataset6)

benfordsprob = [0.301, 0.176, 0.125, 0.097, 0.079, 0.070, 0.060, 0.051, 0.046]

medelvärden = medel(prob1,prob2,prob3,prob4,prob5,prob6)
stdvs = std(medelvärden,prob1,prob2,prob3,prob4,prob5,prob6)
print("medelvärdena är ",medelvärden)
print("\n")
print("standardavvikelsen for siffra n mot medelvärdet för siffra n är ", stdvs)

for n in range(1,10):
    print(np.log10(1+(1/n)), "\n")


'''
print("mse1 ",mse(prob1,benfordsprob))
print("mse2 ",mse(prob2,benfordsprob))
print("mse3 ",mse(prob3,benfordsprob))
print("mse4 ",mse(prob4,benfordsprob))
print("mse5 ",mse(prob5,benfordsprob))
print("mse6 ",mse(prob6,benfordsprob))
print("\n")
print("rmse1 ",rmse(prob1,benfordsprob))
print("rmse2 ",rmse(prob2,benfordsprob))
print("rmse3 ",rmse(prob3,benfordsprob))
print("rmse4 ",rmse(prob4,benfordsprob))
print("rmse5 ",rmse(prob5,benfordsprob))
print("rmse6 ",rmse(prob6,benfordsprob))
print("\n")
print("rmse1 as percentage of mean1 ",rmse(prob1,benfordsprob)/(sum(prob1)/len(prob1)))
print("rmse2 as percentage of mean2 ",rmse(prob2,benfordsprob)/(sum(prob2)/len(prob2)))
print("rmse3 as percentage of mean3 ",rmse(prob3,benfordsprob)/(sum(prob3)/len(prob3)))
print("rmse4 as percentage of mean4 ",rmse(prob4,benfordsprob)/(sum(prob4)/len(prob4)))
print("rmse5 as percentage of mean5 ",rmse(prob5,benfordsprob)/(sum(prob5)/len(prob5)))
print("rmse6 as percentage of mean6 ",rmse(prob6,benfordsprob)/(sum(prob6)/len(prob6)))
'''

plt.bar(digits, prob1, label="IMF ($)")
plt.plot(digits, benfordsprob,"ro", label="According to Benford's law")
plt.plot(digits, benfordsprob,"r-")
plt.xticks(digits, ["1","2","3","4","5","6","7","8","9"])
plt.xlabel("Digits")
plt.ylabel("P(d)")
plt.legend()
plt.show()

plt.bar(digits, prob2, label="IMF (SEK)")
plt.plot(digits, benfordsprob,"ro", label="According to Benford's law")
plt.plot(digits, benfordsprob,"r-")
plt.xticks(digits, ["1","2","3","4","5","6","7","8","9"])
plt.xlabel("Digits")
plt.ylabel("P(d)")
plt.legend()
plt.show()

plt.bar(digits, prob3, label="World Bank ($)")
plt.plot(digits, benfordsprob,"ro", label="According to Benford's law")
plt.plot(digits, benfordsprob,"r-")
plt.xticks(digits, ["1","2","3","4","5","6","7","8","9"])
plt.xlabel("Digits")
plt.ylabel("P(d)")
plt.legend()
plt.show()

plt.bar(digits, prob4, label="World Bank (SEK)")
plt.plot(digits, benfordsprob,"ro", label="According to Benford's law")
plt.plot(digits, benfordsprob,"r-")
plt.xlabel("Digits")
plt.xticks(digits, ["1","2","3","4","5","6","7","8","9"])
plt.ylabel("P(d)")
plt.legend()
plt.show()

plt.bar(digits, prob5, label="CIA ($)")
plt.plot(digits, benfordsprob,"ro", label="According to Benford's law")
plt.plot(digits, benfordsprob,"r-")
plt.xticks(digits, ["1","2","3","4","5","6","7","8","9"])
plt.xlabel("Digits")
plt.ylabel("P(d)")
plt.legend()
plt.show()

plt.bar(digits, prob6, label="CIA (SEK)")
plt.plot(digits, benfordsprob,"ro", label="According to Benford's law")
plt.plot(digits, benfordsprob,"r-")
plt.xticks(digits, ["1","2","3","4","5","6","7","8","9"])
plt.xlabel("Digits")
plt.ylabel("P(d)")
plt.legend()
plt.show()
