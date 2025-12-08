from heapq import heappop, heappush

N, M = map(int, input().split())
A = list(map(int, input().split()))
result = sum(A)
data = []
for a in A:
    heappush(data, -a)

for m in range(M):
    x = -heappop(data)
    tmp = x//2
    result = result - (x - tmp)
    heappush(data, -tmp)

print(result)
