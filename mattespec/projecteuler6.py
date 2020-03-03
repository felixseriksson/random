sumofsquares = 0 
squareofsum = 0

for n in range(1,101):
    sumofsquares = sumofsquares + n**2

sum = int(50*(1+100))

squareofsum = sum**2

diff = squareofsum - sumofsquares

print(diff)