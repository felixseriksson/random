from mypackage import timing
#name: Project Euler 14
#---
#date: "2019-02-11"
#time: "13:44"
#---


maxcounter = 0
maxnumber = 0
for n in range(1000000):
    x = int(n)
    counter = 1
    while x > 0:
        if x == 1:
            break
        elif x % 2 == 0:
            x = int(x/2)
            counter += 1
        elif x % 2 == 1:
            x = int(3*x + 1)
            counter += 1
    if maxcounter < counter:
        maxcounter = counter
        maxnumber = int(n)

print(maxnumber, "has the longest sequence:", maxcounter)