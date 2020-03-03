from mypackage import timing
#name: Project euler 18
#---
#date: "2019-03-18"
#time: "13:23"
#created by Felix Eriksson
#---

'''
pyramid = { "a" : [("b", 3)],
          "b" : [("c", 7), ("d", 4)],
          "c" : [("e",2), ("f",4)],
          "d" : [("f",4), ("g",6)],
          "e" : [("h",8), ("i",5)],
          "f" : [("i",5), ("j",9)],
          "g" : [("j",9), ("k",3)],
        } 

def generate_edges(graph):
    edges = ["a"]

    for node in graph:
        for neighbour in node:
            edge = [node, neighbour]
            return edge

print(generate_edges(pyramid))
'''
graph = [[75],[95,64],[17,47,82],[18,35,87,10],[20,4,82,47,65],[19,1,23,75,3,34],[88,2,77,73,7,63,67],[99,65,4,28,6,16,70,92],[41,41,26,56,83,40,80,70,33],[41,48,72,33,47,32,37,16,94,29],[53,71,44,65,25,43,91,52,97,51,14],[70,11,33,28,77,73,17,78,39,68,17,57],[91,71,52,38,17,14,91,43,58,50,27,29,48],[63,66,4,68,89,53,67,30,73,16,69,87,40,31],[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

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

while x < 16384:
    binary = str(bin(x))
    fixed = binary[2:]
    fixedlist = split(fixed)
    counter = 15 - len(fixedlist)
    if len(fixedlist) < 15:
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