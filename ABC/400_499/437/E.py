import sys
sys.setrecursionlimit(10**6)

def calc(nodes, graph, result):
    nextNodes = []
    for node in nodes:
        tmp = graph.get(node)
        if tmp is None:
            continue
        nextNodes += tmp
    if len(nextNodes) == 0:
        return
    nextNodes.sort()
    prevCost, num = nextNodes[0]
    nextN = []
    for c, num in nextNodes:
        if prevCost != c:
            calc(nextN, graph, result)
            nextN = []
            prevCost = c
            pass
        result.append(num)
        nextN.append(num)
    calc(nextN, graph, result)


N = int(input())
graph = dict()
for n in range(1, N + 1):
    x, y = map(int, input().split())
    tmp = graph.get(x, [])
    tmp.append((y, n))
    graph[x] = tmp
result = []
# print(graph)
calc([0], graph, result)
print(*result)
