from mypackage import timing
#name: project euler 17
#---
#date: "2019-02-28"
#time: "23:10"
#created by Felix Eriksson
#---

ones = ["","one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["","twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

summan = 0

def numberstowords(n):
    if n < 20:
        return ones[n]
    elif n < 100:
        return tens[(n//10)-1]+ones[(n % 10)]
    elif n % 100 == 0 and n != 1000:
        return ones[n // 100]+"hundred"
    elif n < 1000:
        if n//10 % 10 == 1:
            return ones[(n//100)]+"hundredand"+ones[(n % 10)+10]
        elif n // 10 % 10 == 0:
            return ones[(n//100)]+"hundredand"+tens[(((n//10) % 10))]+ones[(n % 10)]
        else:
            return ones[(n//100)]+"hundredand"+tens[(((n//10) % 10))-1]+ones[(n % 10)]
    elif n == 1000:
        return "onethousand"

for n in range(1,1001):
    print(numberstowords(n),n)
    summan += int(len(numberstowords(n)))
print("sum of the letters= ",summan)