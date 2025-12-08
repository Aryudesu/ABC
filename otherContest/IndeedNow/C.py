from heapq import heappop, heappush

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

hp = []
heappush(hp, 1)

result = []
memo = [False] * (N + 1)
memo[1] = True
while hp:
    node = heappop(hp)
    result.append(node)
    for nextNode in graph[node]:
        if memo[nextNode]:
            continue
        heappush(hp, nextNode)
        memo[nextNode] = True
print(*result)
