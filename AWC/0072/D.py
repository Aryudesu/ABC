from collections import defaultdict
from heapq import heappop, heappush

def calc(N: int, P: list[int], graph: dict[int, list[int]])->int:
    result = [0] * N
    data = []
    heappush(data, (P[0], 0))
    result[0] = 1
    while data:
        hgt, pos = heappop(data)
        nextPoss = graph[pos]
        for nextPos in nextPoss:
            nextHgt = P[nextPos]
            nextCnt = result[pos] + 1
            if hgt > nextHgt:
                continue
            if nextCnt > result[nextPos]:
                result[nextPos] = nextCnt
                heappush(data, (nextHgt, nextPos))
    return max(result)


N, M = map(int, input().split())
P = list(map(int, input().split()))
graph = defaultdict(list)
for m in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
res = calc(N, P, graph)
print(res)
