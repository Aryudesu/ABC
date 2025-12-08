from collections import defaultdict

def buildData(start: int, graph: dict[int, list[int]])-> list[int]:
    result: list[int] = [start+1]
    s: int = start + 1
    nodes: set[int] = {start}
    memo: set[int] = {start}
    for i in range(3):
        nextNodes = set()
        for node in nodes:
            for nextNode in graph[node]:
                if nextNode in memo:
                    continue
                nextNodes.add(nextNode)
                memo.add(nextNode)
                s += nextNode + 1
        nodes = nextNodes
        result.append(s)
    return result


graph = defaultdict(list)
N, M = map(int, input().split())
for m in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
data = []
for n in range(N):
    data.append(buildData(n, graph))
result = []
Q = int(input())
for _ in range(Q):
    x, k = map(int, input().split())
    result.append(data[x-1][k])
for r in result:
    print(r)
