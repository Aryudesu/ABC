from heapq import heappop, heappush
from collections import defaultdict

N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
data = []
for i in range(N):
    heappush(data, (-A[i], 1, i))

result = [0] * N
for k in range(K):
    a, c, i = heappop(data)
    result[i] += 1
    heappush(data, (-A[i]/(c + 1), c + 1, i))
print(*result)
