N, M, K = [int(l) for l in input().split()]
graph = dict()
for m in range(M):
    u, v, w = [int(l) for l in input().split()]
    u -= 1
    v -= 1
    tmp = graph.get(u, [])
    tmp.append((v, w))
    graph[u] = tmp
    tmp = graph.get(v, [])
    tmp.append((u, w))
    graph[v] = tmp
nodes = [False] * N
data = [0] * N
node_num = 0
weight_sum = 0

def calc(node, weight):
    node_num += 1

