xstart = input("startvärde för x = ")
ystart = input("startvärde för y = ")
xstop = float(input("stoppvärde för x = "))
steglängd = float(input("steglängd = "))

x = float(xstart)
y = float(ystart)

while x < xstop:
    yprim = 2*x
    y = float(y + yprim*steglängd)
    x += float(steglängd)

print("när x = ", xstop, "så är y ungefär = ", y)