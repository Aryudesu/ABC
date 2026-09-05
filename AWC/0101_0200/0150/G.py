from atcoder.scc import SCCGraph

N, Q = map(int, input().split())
T = list(map(int, input().split()))
scc = SCCGraph(N)
for n in range(N):
    scc.add_edge(n, T[n] - 1)
sG = scc.scc()
data = [None] * N
graph = [[] for _ in range(N)]
for g in sG:
    if len(g) > 1:
        for c in g:
            data[c] = len(g)
leaf = set()
for g in sG:
    if len(g) == 1:
        for c in g:
            graph[T[c]-1].append(c)
            if data[T[c]-1] is not None:
                leaf.add(T[c] - 1)
nodes = leaf
while nodes:
    nextNodes = set()
    for node in nodes:
        for nextNode in graph[node]:
            data[nextNode] = data[node] + 1
            nextNodes.add(nextNode)
    nodes = nextNodes
# print(data)

result = []
for _ in range(Q):
    s = int(input())
    result.append(data[s-1])
print(*result, sep="\n")
