from sortedcontainers import SortedSet
N, K = map(int, input().split())
A = list(map(int, input().split()))
data = SortedSet()
for a in A:
    data.add(a % K)
M = len(data)
result = data[-1] - data[0]
for _ in range(M):
    tmp = data.pop()
    tmp = tmp - K
    data.add(tmp)
    res = data[-1] - data[0]
    result = min(result, res)
print(result)
