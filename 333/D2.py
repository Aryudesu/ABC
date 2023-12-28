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

data = []
one_nodes = graph.get(0, [])
node_data = [False] * N
node_data[0] = True
for on in one_nodes:
    res = 1
    nodes = set(graph.get(on, []))
    while nodes:
        new_nodes = set()
        for nn in nodes:
            for nm in graph.get(nn, []):
                if not node_data[nm]:
                    node_data[nm] = True
                    new_nodes.add(nn)
                    res += 1
        nodes = new_nodes
    data.append(res)
data.sort()
print(sum(data) - data[-1] + 1)
