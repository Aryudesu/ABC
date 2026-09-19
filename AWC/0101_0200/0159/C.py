N, M, K = map(int, input().split())
switchs = []
for m in range(M):
    c, *S = list(map(int, input().split()))
    num = 0
    for s in S:
        num |= 1 << (s-1)
    switchs.append(num)

isOk = False
result = M
for mask in range(1 << M):
    tmp = 0
    for m in range(M):
        b = mask & (1 << m)
        if b:
            tmp ^= switchs[m]
    if tmp.bit_count() == K:
        isOk = True
        result = min(result, mask.bit_count())
print(result if isOk else -1)
