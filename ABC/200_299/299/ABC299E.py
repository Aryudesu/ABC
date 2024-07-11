def get_dist_node(depth, result, graph, node, nodes):
    if depth == 0:
        result.add(node)
    nds = graph.get(node, [])
    for nd in nds:
        if not nodes[nd]:
            nodes[nd] = True
            get_dist_node(depth-1, result, graph, nd, nodes)
            nodes[nd] = False


N, M = [int(l) for l in input().split()]
graph = dict()
for m in range(M):
    u, v = [int(l) for l in input().split()]
    tmp = graph.get(u, [])
    tmp.append(v)
    graph[u] = tmp
    tmp = graph.get(v, [])
    tmp.append(u)
    graph[v] = tmp
K = int(input())
nodes = [False] * (N + 1)
n_c = dict()
for _ in range(K):
    p, d = [int(l) for l in input().split()]
    tmp = set()
    nodes[p] = True
    get_dist_node(d, tmp, graph, p, nodes)
    nodes[p] = False
    t = n_c.get(p, [])
    t.append(tmp)
    n_c[p] = t
print(nodes)
print(n_c)
