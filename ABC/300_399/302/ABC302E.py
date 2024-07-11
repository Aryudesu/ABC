N, Q = [int(l) for l in input().split()]
graph = dict()
node = {i for i in range(N)}
for q in range(Q):
    num, *query = [int(l) for l in input().split()]
    if num == 1:
        u, v = query[0] - 1, query[1] - 1
        tmp = graph.get(u, set())
        tmp.add(v)
        graph[u] = tmp
        tmp = graph.get(v, set())
        tmp.add(u)
        graph[v] = tmp
        node.discard(u)
        node.discard(v)
    elif num == 2:
        v = query[0] - 1
        tmp = graph.get(v, set())
        for t in tmp:
            graph[t].discard(v)
            if len(graph.get(t, set())) == 0:
                node.add(t)
        graph[v] = set()
        node.add(v)
    print(len(node))
