#det här programmet beräknar fakultet

tal = int(input("Ange ditt tal: "))

i = 1
fakultet = 1

while (i<= tal):
    fakultet = fakultet*i
    i=i+1

print("fakulteten blir: ", fakultet)