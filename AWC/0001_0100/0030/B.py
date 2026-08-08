INF = 10 ** 10
N, M = map(int, input().split())
PT = []
for n in range(N):
    p, t = map(int, input().split())
    PT.append((p, t))
for m in range(M):
    K, *S = map(int, input().split())
    zeroMin = INF
    oneMin = INF
    for s in S:
        if PT[s-1][1] == 0:
            zeroMin = min(zeroMin, PT[s-1][0])
        if PT[s-1][1] == 1:
            oneMin = min(oneMin, PT[s-1][0])
    if zeroMin < INF and oneMin < INF:
        print(zeroMin + oneMin)
    else:
        print(-1)
