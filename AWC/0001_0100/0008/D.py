from heapq import heappop, heappush

N, M = map(int, input().split())
data = []
for n in range(N):
    f, d = map(int, input().split())
    heappush(data, (-f, d))
result = 0
for m in range(M):
    f, d = heappop(data)
    result += -f
    heappush(data, (min(f+d, 0), d))
print(result)
