from collections import defaultdict

N, M, L, S, T = map(int, input().split())
graph = defaultdict(list)
for m in range(M):
    u, v, c = map(int, input().split())
    graph[u-1].append((v-1, c))
nodes = {(0, 0)}
for l in range(L):
    nextNodes = set()
    for node, cost in nodes:
        for n, c in graph[node]:
            next_cost = cost + c
            if next_cost > T:
                continue
            next_node = n
            nextNodes.add((next_node, next_cost))
    nodes = nextNodes
result = []
memo = set()
for n, c in nodes:
    if S <= c <= T:
        if n in memo:
            continue
        result.append(n+1)
        memo.add(n)
result.sort()
print(*result)
