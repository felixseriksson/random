def f(x, y):
    if x > y:
        return x + y
    else:
        return f(x+y, y-x)
    
print(f(0, 10))