from collections import deque
def bfs(array, x, y, visited):
    q = deque()
    q.append((x,y))
    pop = 0
    while q:
        v = q.popleft()
        if v in visited:
            continue
        visited.add(v)
        pop += 1
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        toaddtoq = [tuple(map(lambda i, j: i + j, v, ofs)) for ofs in offsets]
        for val in toaddtoq:
            if not val in visited:
                q.append(val)
    return pop, visited

testcases = int(input())
for testcase in range(testcases):
    n, m = [int(x) for x in input().split()]
    array = [[0]*(m+2)]
    for line in range(n):
        array.append([0] + [int(x) for x in input().split()] + [0])
    array.append([0]*(m+2))
    
    pop = 0
    troops = 0
    visited = set()

    for i in range(n+2):
        for j in range(m+2):
            if array[i][j] == 0:
                visited.add((i, j))

    for linenum in range(1, n + 1):
        for colnum in range(1, m + 1):
            if not (linenum, colnum) in visited:
                newpop, visited = bfs(array, linenum, colnum, visited)
                pop = max(newpop, pop)
                troops += 1
    print(troops, pop)