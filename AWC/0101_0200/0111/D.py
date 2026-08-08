def calc(node: int, prev: int, graph: list[list[int]], data: list[str], result: set[str]):
    nextNodes = graph[node]
    for nextNode in nextNodes:
        if nextNode == prev:
            continue
        data.append()


N = int(input())
graph1 = [[] for _ in range(N)]
for _ in range(N-1):
    ua, va = map(int, input().split())
    graph1[ua-1].append(va-1)
    graph1[va-1].append(ua-1)

graph2 = [[] for _ in range(N)]
for _ in range(N-1):
    ub, vb = map(int, input().split())
    graph2[ub-1].append(vb-1)
    graph2[vb-1].append(ub-1)

