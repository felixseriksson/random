from functools import reduce
from operator import mul
for i in range(100, 1000):
    nums = [a for a in range(1, i+1) if i % a == 0]
    if abs(22 - (reduce(mul, nums))**(1/len(nums))) < 0.001:
        print(i)