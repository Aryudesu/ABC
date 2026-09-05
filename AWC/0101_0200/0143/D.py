from sortedcontainers import SortedList

N, Q = map(int, input().split())
S = list(map(int, input().split()))
data = SortedList(S)
result = []
for _ in range(Q):
    t, v = map(int, input().split())
    data.discard(S[t-1])
    data.add(v)
    S[t-1] = v
    kijun = data[(N + 1)//2 - 1]
    result.append(data.bisect_left(kijun))
    # print(data)
print(*result, sep="\n")
