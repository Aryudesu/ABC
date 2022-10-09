N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]

vals = [set() for _ in range(M)]

# 取りうる値の表を作る
for n in range(N):
    a = A[n]
    idx = 0
    if a < 0:
        idx = -a // (n + 1)
        print(idx)
    if a + (n + 1) * M < 0:
        continue
    if a >= N:
        continue
    for m in range(idx-1, M):
        a += (n + 1)
        if a >= N:
            break
        if a < 0:
            continue
        vals[m].add(a)
print(vals)
# M回やる
for m in range(M):
    res = 0
    size = len(vals[m])
    for i in range(size):
        if i in vals[m]:
            res += 1
        else:
            break
    print(res)
