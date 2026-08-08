def calcDFS(graph: list[list[int]], start: int, depth: int, V: list[int])->list[int]:
    result = []
    nodes = set()
    memo = set()
    for node in graph[start]:
        nodes.add(node)
    for startNextNode in nodes:
        memo.add(start)
        memo.add(startNextNode)
        s = V[startNextNode]
        for d in range(depth):
            nextNodes = set()
            for node in nodes:
                for nextNode in graph[node]:
                    if nextNode in memo:
                        continue
                    nextNodes.add(nextNode)
                    memo.add(nextNode)
                    s += V[nextNode]
            nodes = nextNodes
        result.append(s)
    return result

N, D = map(int, input().split())
V = list(map(int, input().split()))
vsum = sum(V)
graph = [[] for _ in range(N)]
for n in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
result1 = vsum
result2 = vsum
for start in range(N):
    res = calcDFS(graph, start, D, V)
    for r in res:
        val = r + V[start]
        if val < result2:
            result2 = val
            resul1 = val
