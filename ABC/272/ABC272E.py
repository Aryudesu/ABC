N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
vals = [[] for _ in range(M + 1)]
for i in range(N):
    if A[i] >= N:
        continue
    l = 1 if A[i] >= 0 else (-A[i] + i) // (i + 1)
    r = min([M + 1, (N - A[i] + i) // (i + 1)])
    for j in range(l, r):
        vals[j].append(A[i] + (i + 1) * j)
print(vals)
for i in range(1, M + 1):
    sz = len(vals[i])
    exi = [False for _ in range(sz + 1)]
    for v in vals[i]:
        if v < sz:
            exi[v] = True
    res = 0
    while exi[res]:
        res += 1
    print(res)
