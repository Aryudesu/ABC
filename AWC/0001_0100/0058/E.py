from sortedcontainers import SortedList

N, K = map(int, input().split())
A = list(map(int, input().split()))
data = SortedList()
lIdx = 0
result = 0
for r in range(N):
    data.add(A[r])
    while data and data[-1] - data[0] > K:
        data.discard(A[lIdx])
        lIdx += 1
    result = max(result, len(data))
print(result)
