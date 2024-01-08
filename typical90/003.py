import sys

sys.setrecursionlimit(10**6)

N = int(input())
graph = dict()
for n in range(N-1):
    a, b = [int(l) for l in input().split()]
    tmp = graph.get(a, [])
    tmp.append(b)
    graph[a] = tmp
    tmp = graph.get(b, [])
    tmp.append(a)
    graph[b] = tmp

memo = [False for _ in range(N + 1)]

def calc(depth, n):
    nodes = graph.get(n)
    memo[n] = True
    res_depth, res_node = -1, None
    for node in nodes:
        if memo[node]:
            continue
        tmpres, tmpnode = calc(depth + 1, node)
        if res_depth < tmpres:
            res_depth = tmpres
            res_node = tmpnode
    memo[n] = False
    if res_depth < 0:
        return depth, n
    return res_depth, res_node

def calc2(depth, n, m):
    if n == m:
        return depth
    nodes = graph.get(n)
    memo[n] = True
    res_depth = -1
    for node in nodes:
        if memo[node]:
            continue
        tmpres = calc2(depth + 1, node, m)
        if res_depth < tmpres:
            res_depth = tmpres
    memo[n] = False
    return res_depth

rd1, rn1 = calc(1, 1)
rd2, rn2 = calc(1, rn1)
rd3 = calc2(1, rn1, rn2)
print(rd3)
