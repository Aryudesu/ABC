N, Q = [int(l) for l in input().split()]
A = [int(l) for l in ('0 ' + input()).split()]
s = 0
S = []
for a in A:
    s += a
    S.append(s)
res = []
for q in range(Q):
    L, R = [int(l) for l in input().split()]
    res.append(S[R] - S[L - 1])
for r in res:
    print(r)
