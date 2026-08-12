def calc(graph: list[list[int]], K: int)->int:
    nodes = {K}
    result = {K}
    while nodes:
        nextNodes = set()
        for node in nodes:
            for nextNode in graph[node]:
                result.add(nextNode)
                nextNodes.add(nextNode)
        nodes = nextNodes
    return len(result)
    

N, K = map(int, input().split())
graph = [[] for _ in range(N)]
P = [-1]
if N > 1:
    P = [-1] + list(map(int, input().split()))
for idx in range(1, N):
    child = idx
    parent = P[idx] - 1
    graph[parent].append(child)
res = calc(graph, K-1)
print(N-res)
