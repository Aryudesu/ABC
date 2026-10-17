import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)

def countDFS(graph: list[list[int]], root: int = 0, prev: int = -1)->int:
    res = 0
    for nextNode in graph[root]:
        if nextNode == prev:
            continue
        res += countDFS(graph, nextNode, root)
    COUNTS[root] = res + 1
    PARENTS[root] = prev
    return res + 1

def calcDFS(graph: list[list[int]], sm: int, root: int = 0, prev: int = -1):
    nextSum = sm + IMOS[root]
    RESULT[root] = nextSum
    for nextNode in graph[root]:
        if nextNode == prev:
            continue
        calcDFS(graph, nextSum, nextNode, root)
    

N = int(input())
graph = [[] for _ in range(N)]
edge = []
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    edge.append((a, b))
COUNTS = [0] * N
PARENTS = [-1] * N
IMOS = [0] * (N + 1)
countDFS(graph)

for n in range(N-1):
    a, b = edge[n]
    a, b = a-1, b-1
    if PARENTS[b] == a:
        a, b = b, a
    ca = COUNTS[a]
    cb = N - COUNTS[a]
    # print("debug", ca, cb)
    if ca > cb:
        IMOS[a] += n + 1
    else:
        IMOS[a] -= n + 1
        IMOS[0] += n + 1

RESULT = [0] * N
calcDFS(graph, 0)
print(*RESULT)
