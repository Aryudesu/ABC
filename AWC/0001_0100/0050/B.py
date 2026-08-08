from heapq import heappop, heappush

N, K = map(int, input().split())
data = []
for n in range(N):
    a, b = map(int, input().split())
    heappush(data, (-min(a, b), -a, -b))

result = 0
for k in range(K):
    n, a, b = heappop(data)
    a = -a
    b = -b
    result += -n
    a += n
    heappush(data, (-min(a, b), -a, -b))
    # print(data)
print(result)
