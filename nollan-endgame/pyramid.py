graph = [[75],[95,64],[17,47,82],[18,35,87,10],[20,4,82,47,65],[19,1,23,75,3,34],[88,2,77,73,7,63,67],[99,65,4,28,6,16,70,92],[41,41,26,56,83,40,80,70,33]]

# ovan ger fel svar 472, nedan ger kanske rätt svar 649
# nvm hade "while x < 2^8" dvs "x < 10" istället för "x < 2**8" dvs "x < 256"
#'''

längstaväg = 0

x = 0

def split(word): 
    return [int(char) for char in word]  

def väg(lista):
    summan = 0  
    place = 0
    element = 0
    for n in lista:
        element += n
        summan += graph[place][element]
        place += 1
    return summan

while x < 2**8:
    binary = str(bin(x))
    fixed = binary[2:]
    fixedlist = split(fixed)
    counter = 9 - len(fixedlist)
    if len(fixedlist) < 9:
        for n in range(counter):
            fixedlist.insert(0,0)
        print(fixed)
        print(fixedlist)
    vägen = väg(fixedlist)
    if vägen > längstaväg:
        längstaväg = vägen
    print(vägen)
    print(längstaväg)
    x += 1



print("den längsta vägen är ",längstaväg)

#'''
'''
data = graph
max_sum = 0
def find_sums(r=0,c=0,total=0):
	global max_sum
	total += data[r][c]
	if r == len(data) - 1:
		if total > max_sum:
			max_sum = total
		return
	else:
		find_sums(r+1,c,total)
		find_sums(r+1,c+1,total)
find_sums()
print(max_sum)
'''