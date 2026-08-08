from sortedcontainers import SortedList

INF = 10 ** 18
N, K, T = map(int, input().split())
S = list(map(int, input().split()))
T -= 1
S[T] = 0
data = SortedList()
for k in range(K):
    data.add(S[k])
result = -INF
if 0 <= T < K:
    result = min(0, data[0])
for l in range(N-K):
    r = l + K
    data.discard(S[l])
    data.add(S[r])
    if l + 1 <= T <= r:
        # print(l + 1, r)
        # print(S)
        # print(data)
        result = max(result, data[0])
print(result)
