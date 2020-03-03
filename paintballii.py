# from collections import defaultdict, deque

# opponentsnum = int(input())
# opponents = []

# for n in range(opponentsnum):
#     opponents.append(tuple([int(x) for x in input().split()]))

# print(opponents)
# edges = defaultdict(list)

# startafrån = []

# while opponents:
#     op = opponents.pop()
#     if op[1]-op[2] <= 0: #samma som nedan
#         startafrån.append(op)
#     for other in opponents:
#         combrange = op[2] + other[2]
#         dist = (((op[0]-other[0])**2)+((op[1]-other[1])**2))**0.5
#         if combrange >= dist: #ska det vara större eller lika med om man måste vara strikt innanför range:n?
#             edges[op].append(other)
#             edges[other].append(op)
# print(edges)
# print(startafrån)

# def bfs(visited, edges, node):
#     visited.append(node)
#     queue.append(node)

#     while queue:
#         s = queue.popleft()

#         if s[1] + s[2] >= 1000: #samma som ovan
#             return False

#         for neighbour in edges[s]:
#             if neighbour not in visited:
#                 visited.append(neighbour)
#                 queue.append(neighbour)
#     return visited

# visited = []
# for start in startafrån:
#     queue = deque()
#     try:
#         visited = bfs(visited, edges, start)
#     except:
#         print("IMPOSSIBLE")

'''
ny idé: generera "hinder" som linjer mellan två mittpunkter där cirklarna skär varandra, samt kolla för varja cirkel
i samma vända vilka startpunkter på vänsterkanten och slutpunkter på högerkanten den utesluter (om några)
kör sedan bfs på alla kvarvarande startpunkter och se om nån når (börja norrifrån för att garanterat hitta de mest norra då vägar ej korsas)
'''
from collections import defaultdict, deque

opponentsnum = int(input())
opponents = []

for n in range(opponentsnum):
    opponents.append(tuple([int(x) for x in input().split()]))

print(opponents)
grid = [[1]*1001 for n in range(1001)]
print(grid)

def get_line(start, end):
    """Bresenham's Line Algorithm
    Produces a list of tuples from start and end
 
    points1 = get_line((0, 0), (3, 4))
    points2 = get_line((3, 4), (0, 0))
    assert(set(points1) == set(points2))
    print points1
    [(0, 0), (1, 1), (1, 2), (2, 3), (3, 4)]
    print points2
    [(3, 4), (2, 3), (1, 2), (1, 1), (0, 0)]
    """
    # Setup initial conditions
    x1, y1 = start[0], start[1]
    x2, y2 = end[0], end[1]
    dx = x2 - x1
    dy = y2 - y1
 
    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)
 
    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
 
    # Swap start and end points if necessary and store swap state
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
 
    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1
 
    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1
 
    # Iterate over bounding box generating points between start and end
    y = y1
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        grid[coord[1]][coord[0]] = False
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx
 
    # Reverse the list if the coordinates were swapped
    return

inrangeleft = []
inrangeright = []

while opponents:
    op = opponents.pop()
    if op[0]-op[2] <= 0: #samma som nedan
        inrangeleft.append(op)
    if op[0] + op[2] >= 1000:
        inrangeright.append(op)
    for other in opponents:
        combrange = op[2] + other[2]
        dist = (((op[0]-other[0])**2)+((op[1]-other[1])**2))**0.5
        if combrange >= dist: #ska det vara större eller lika med om man måste vara strikt innanför range:n?
           get_line(op, other)
           print(grid)

print(grid)

def bfs(visited, edges, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.popleft()

        if s[1] + s[2] >= 1000: #samma som ovan
            return False

        for neighbour in edges[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return visited

visited = []
for start in startafrån:
    queue = deque()
    try:
        visited = bfs(visited, edges, start)
    except:
        print("IMPOSSIBLE")