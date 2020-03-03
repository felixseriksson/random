from mypackage import timing
#name: Project Euler 67
#---
#date: "2019-04-11"
#time: "12:52"
#created by Felix Eriksson
#---

from collections import deque, namedtuple

inf = float("inf")
edge = namedtuple("edge", "start, end, costs")

def make_edge(start, end, cost = 1):
    return edge(start, end, cost)

