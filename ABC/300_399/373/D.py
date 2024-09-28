import sys

import pypyjit

pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**7)

N, M = [int(l) for l in input().split()]
result = [None] * N
INF = 10 ** 18

def calc(node, graph, MAXNum, MINNum):
    next_node = graph.get(node, set())
    for v, w in next_node:
        if not result[v] is None:
            continue
        tmp = result[node] + w
        if tmp < MINNum:
            MINNum = tmp
        if tmp > MAXNum:
            MAXNum = tmp
        result[v] = tmp
        newMax, newMin = calc(v, graph, MAXNum, MINNum)
        MAXNum = max([newMax, MAXNum])
        MINNum = min([newMin, MINNum])
    return MAXNum, MINNum

graph = dict()
for m in range(M):
    u, v, w = [int(l) for l in input().split()]
    u, v = u-1, v-1
    tmp = graph.get(u, set())
    dat = (v, w)
    tmp.add(dat)
    graph[u] = tmp
    tmp = graph.get(v, set())
    dat = (u, -w)
    tmp.add(dat)
    graph[v] = tmp
MAX = -INF
MIN = INF
for i in range(N):
    if result[i] is None:
        result[i] = 0
        MAX, MIN = calc(i, graph, MAX, MIN)
if MAX > INF:
    for i in range(N):
        result[i] += INF - MAX
if MIN < -INF:
    for i in range(N):
        result[i] += INF - MIN
print(*result)
