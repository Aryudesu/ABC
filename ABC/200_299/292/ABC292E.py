N, M = [int(l) for l in input().split()]
graph = dict()
for n in range(N):
    u, v = [int(l) for l in input().split()]
    tmp = graph.get(u, [])
    tmp.append(v)
    graph[u] = tmp
    tmp = graph.get(v, [])
    tmp.append(u)
    graph[v] = tmp
