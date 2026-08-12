from sortedcontainers import SortedList

N, M, K, T = map(int, input().split())
result = 0
for n in range(N):
    S = list(map(int, input().split()))
    data = SortedList(S[:K])
    res = data[-1] - data[0]
    if res >= T:
        result += 1
        continue
    for r in range(K, M):
        data.discard(S[r-K])
        data.add(S[r])
        # print(data)
        res = data[-1] - data[0]
        # print("debug", res)
        if res >= T:
            result += 1
            break
print(result)
