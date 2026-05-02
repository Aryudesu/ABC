N, M, K = map(int, input().split())
T = list(map(int, input().split()))
data = []
senkou = []
for n in range(N):
    S = list(map(int, input().split()))
    isOk = True
    for m in range(M):
        if S[m] < T[m]:
            isOk = False
    if isOk:
        senkou.append(n)
        data.append((sum(S), n))

result = []
if len(senkou) <= K:
    result = senkou
else:
    data.sort(reverse=True)
    B = data[K-1][0]
    result = []
    for s, n in data:
        if s < B:
            break
        result.append(n)
    result.sort()
for r in result:
    print(r + 1)
