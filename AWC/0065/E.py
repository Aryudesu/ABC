from sortedcontainers import SortedList

N, K, D = map(int, input().split())
H = list(map(int, input().split()))
data = SortedList()
result = 0
l = 0
for r in range(N):
    data.add(H[r])
    while data[-1] - data[0] > D:
        data.remove(H[l])
        l += 1
    if len(data) >= K:
        result = max(result, len(data))
print(result if result >= K else -1)
