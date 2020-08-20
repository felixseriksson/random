ctr = 0
num = 1
while True:
    length  = len(str(num))
    unique = len(set([char for char in str(num)]))
    if length == unique:
        ctr += 1
    if ctr == 1000:
        print("1000nde är: ", num)
        break
    num += 1