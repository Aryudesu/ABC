N = int(input())
nodes = {l + 1 for l in range(N)}
data = [0] * (N + 1)
graph = dict()
result = []
for n in range(N - 1):
    u, v = [int(l) for l in input().split()]
    tmp = graph.get(u, [])
    tmp.append(v)
    graph[u] = tmp
    tmp = graph.get(v, [])
    tmp.append(u)
    graph[v] = tmp
    data[u] += 1
    data[v] += 1
for i in range(1, N + 1):
    d = data[i]
    if d <= 2:
        continue
    tmp = graph.get(i, [])
    if i in nodes:
        result.append(d)
        nodes.remove(i)
    for t in tmp:
        if t in nodes:
            nodes.remove(t)
for i in range(len(nodes) // 3):
    result.append(2)
result.sort()
print(*result)
