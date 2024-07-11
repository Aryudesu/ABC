import sys

import pypyjit

pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)

N = int(input())
graph = dict()
for n in range(N-1):
    u, v = [int(l) - 1 for l in input().split()]
    tmp = graph.get(u, [])
    tmp.append(v)
    graph[u] = tmp
    tmp = graph.get(v, [])
    tmp.append(u)
    graph[v] = tmp
nodes = [False] * N

def calc(node):
    nodes[node] = True
    res = 0
    kk = graph.get(node, [])
    for k in kk:
        if nodes[k]:
            continue
        res += calc(k)
    nodes[node] = False
    res += 1
    return res

nodes[0] = True
on = graph.get(0, [])
datas = []
for n in on:
    datas.append(calc(n))
datas.sort()
result = sum(datas) - datas[-1]
print(result + 1)
