from sortedcontainers import SortedList

N, K = map(int, input().split())
H = list(map(int, input().split()))
data = SortedList()
for i in range(K):
    data.add(H[i])
result = data[-1] - data[0]
for i in range(N - K):
    data.discard(H[i])
    data.add(H[i + K])
    result = max(result, data[-1] - data[0])
print(result)
