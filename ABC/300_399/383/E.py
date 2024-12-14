N, M, K = [int(l) for l in input().split()]
graph = dict()
for m in range(M):
    u, v, w = [int(l) for l in input().split()]
    tmp = graph.get(u, [])
    tmp.append([v, w])
    graph[u] = tmp
    tmp = graph.get(v, [])
    tmp.append([u, w])
    graph[v] = tmp
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
