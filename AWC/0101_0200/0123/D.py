from heapq import heappush, heappop
from atcoder.scc import SCCGraph

N, M = map(int, input().split())
parents = set(range(N))
graph = [[] for _ in range(N)]
nums = [0] * N
scc = SCCGraph(N)
for m in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    scc.add_edge(a-1, b-1)
    parents.discard(b-1)
    nums[b-1] += 1
sccData = scc.scc()
if N > 1 and len(sccData) != N:
    print(-1)
    exit(0)
elif N == 1:
    print(1)
    exit(0)
data = []
for p in parents:
    heappush(data, p)
result = []
while data:
    node = heappop(data)
    result.append(node + 1)
    for nextNode in graph[node]:
        nums[nextNode] -= 1
        if nums[nextNode] == 0:
            heappush(data, nextNode)
print(*result)
