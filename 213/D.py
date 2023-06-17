import sys
sys.setrecursionlimit(10**6)


def calc(node_num, graph, result, yet):
    result.append(node_num)
    nodes = graph.get(node_num, [])
    for node in nodes:
        move = False
        if yet[node]:
            yet[node] = False
            move = True
            calc(node, graph, result, yet)
        if move:
            result.append(node_num)


N = int(input())
yet = [True] * (N+1)
graph = dict()
for n in range(N-1):
    a, b = [int(l) for l in input().split()]
    tmp = graph.get(a, [])
    tmp.append(b)
    graph[a] = tmp
    tmp = graph.get(b, [])
    tmp.append(a)
    graph[b] = tmp
for k in graph:
    tmp = graph.get(k, [])
    tmp.sort()
    graph[k] = tmp

result = []
yet[1] = False
calc(1, graph, result, yet)
print(*result)
