def calc(N, graph):
    memo = [False] * N
    nodes = set()
    nodes.add(0)
    result = 0
    while nodes:
        new_nodes = set()
        for node in nodes:
            gh = graph.get(node, [])
            for g in gh:
                if memo[g]:
                    continue
                memo[g] = True
                new_nodes.add(g)
        result += 1
        if 0 in new_nodes:
            return result
        nodes = new_nodes
    return -1


N, M = [int(l) for l in input().split()]
graph = dict()
for m in range(M):
    a, b = [int(l) - 1 for l in input().split()]
    tmp = graph.get(a, [])
    tmp.append(b)
    graph[a] = tmp
print(calc(N, graph))
