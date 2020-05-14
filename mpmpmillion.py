def func(num, ival, jval):
    if num in funcmemo:
        return funcmemo[num]
    elif num == 0:
        val = ival
    elif num == 1:
        val = jval
    else:
        val = funcmemo[num-1] + funcmemo[num-2]
    funcmemo[num] = val
    return val
maxi = None
maxj = None
maxiter = 0

for i in range(500000):
    for j in range(500000):
        if i == 0 and j == 0:
            continue
        funcmemo = {}
        iterr = 0
        while True:
            returned = func(iterr, i, j)
            if returned == 1000000:
                print("first value {} and second value {} reach 1 million in {} iterations".format(i, j, iterr))
                if iterr > maxiter:
                    maxiter = iterr
                    maxi = i
                    maxj = j
                break
            elif returned > 1000000:
                print("didn't reach exactly 1 million for first value {} and second value {} :( (broke at {})".format(i, j, iterr))
                break
            else:
                iterr +=1
                continue

print("best results reached with i = {}, j = {} ({} iterations to reach 1 mill)".format(maxi, maxj, maxiter))