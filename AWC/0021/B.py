N, M = map(int, input().split())
P = list(map(int, input().split()))
result = []
for n in range(N):
    k, *C = list(map(int, input().split()))
    if k == 0:
        result.append(0)
        continue
    maxIdx = 0
    maxScr = -1
    for c in C:
        if P[c-1] > maxScr:
            maxScr = P[c-1]
            maxIdx = c
        elif P[c-1] == maxScr:
            maxIdx = min(maxIdx, c)
    result.append(maxIdx)
for r in result:
    print(r)
