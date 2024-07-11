import bisect

N, K = [int(l) for l in input().split()]
P = [int(l) for l in input().split()]
f = []
fm = []
res = [-1] * N
m = 0
for i in range(N):
    if P[i] > m:
        f.append(P[i])
        fm.append([P[i]])
        idx = len(f) - 1
        m = P[i]
    else:
        idx = bisect.bisect_left(f, P[i])
        tmp = f[idx]
        fm[idx].append(P[i])
        if tmp == f[-1]:
            m = P[i]
        f[idx] = P[i]
    if len(fm[idx]) == K:
        for me in fm[idx]:
            res[me - 1] = i + 1
        fm.pop(idx)
        f.pop(idx)
        m = f[-1] if len(f) > 0 else 0
for r in res:
    print(r)
