N, S = map(int, input().split())
INF = N + 5
A = list(map(int, input().split()))
data = [INF] * (S + 2)
data[0] = 0
for a in A:
    for s in range(S + 1, -1, -1):
        nowNum = data[s]
        if nowNum > N:
            continue
        nextNum = nowNum + 1
        nextS = s + a
        if nextS >= S + 2:
            continue
        data[nextS] = min(data[nextS], nextNum)
print(data[S] if data[S] < INF else -1)
