INF = 2 ** 61

def calc(graph, node, memo, N, res = 0):
    if node == N:
        return res
    next_node = graph.get(node, [])
    result = INF
    for u, w in next_node:
        if u in memo:
            continue
        memo.add(u)
        r = calc(graph, u, memo, N, res ^ w)
        memo.discard(u)
        if r < result:
            result = r
    return result

N, M = [int(l) for l in input().split()]
graph = dict()
memo = set()
for m in range(M):
    u, v, w = [int(l) for l in input().split()]
    tmp = graph.get(u, [])
    tmp.append((v, w))
    graph[u] = tmp
    tmp = graph.get(v, [])
    tmp.append((u, w))
    graph[v] = tmp

memo.add(1)
res = calc(graph, 1, memo, N)
print(res)
