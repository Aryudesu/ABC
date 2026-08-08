INF = 10 ** 18
N, K, M = map(int, input().split())
S = list(map(int, input().split()))
LRP = []
for m in range(M):
    l, r, p = map(int, input().split())
    LRP.append((l, r, p))

result = -INF
for mask in range(1 << N):
    if mask.bit_count() > K:
        continue
    sRes = 0
    for idx in range(N):
        b = 1 << idx
        if b & mask != 0:
            sRes += S[idx]

    pRes = 0
    for l, r, p in LRP:
        for idx in range(l-1, r):
            b = 1 << idx
            if b & mask == 0:
                continue
            pRes += p
            break
    result = max(result, sRes + pRes)
print(result)
