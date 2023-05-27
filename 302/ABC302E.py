N, Q = [int(l) for l in input().split()]
# data = {n + 1 for n in range(N)}
graph = dict()
ny_node = set()
for q in range(Q):
    query = [int(l) for l in input().split()]
    if query[0] == 1:
        tmp = graph.get(query[1])
        if tmp is None:
            tmp = set()
        tmp.add(query[2])
        graph[query[1]] = tmp
        tmp = graph.get(query[2])
        if tmp is None:
            tmp = set()
        tmp.add(query[1])
        graph[query[2]] = tmp
        if query[1] in ny_node:
            ny_node.remove(query[1])
        if query[2] in ny_node:
            ny_node.remove(query[2])
    elif query[0] == 2:
        graph[query[1]] = set()
        ny_node.add(query[1])
    else:
        raise Exception()
    res = set()
    for g in graph:
        res = res | graph.get(g)
    print(res - ny_node)
    print(N - len(res - ny_node))
