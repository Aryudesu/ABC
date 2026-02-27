from collections import defaultdict
from heapq import heappop, heappush

INF = 10**18

graph = defaultdict(list)
N, M = map(int, input().split())
for m in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# (頂点番号, 距離)
data = []
heappush(data, (0, 1))
length = defaultdict(lambda:INF)
length[1] = 0
prevData = defaultdict(set)
while data:
    l, pos = heappop(data)
    if l > length[pos]:
        continue
    for nextPos, w in graph[pos]:
        nextL = l + w
        if length[nextPos] < nextL:
            continue
        if length[nextPos] == nextL:
            prevData[nextPos].add(pos)
            continue
        else:
            prevData[nextPos] = {pos}
        length[nextPos] = nextL
        heappush(data, (nextL, nextPos))
result = 1
nowNode = [N]
memo = [False] * (N + 1)
while nowNode:
    nextNode = []
    for node in nowNode:
        for i in prevData[node]:
            if memo[i]:
                continue
            nextNode.append(i)
            memo[i] = True
            result += 1
    nowNode = nextNode
print(result)
