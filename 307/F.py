N, M = [int(l) for l in input().split()]
graph = dict()
for m in range(M):
    U, V, W = [int(l) for l in input().split()]
    tmp = graph.get(U, [])
    tmp.append((V, W))
    graph[U] = tmp
    tmp = graph.get(V, [])
    tmp.append((U, W))
    graph[V] = tmp
K = int(input())
A = [int(l) for l in input().split()]
D = int(input())
X = [int(l) for l in input().split()]
