N, Q = [int(l) for l in input().split()]
A = []
L = []
for n in range(N):
    l, *a = [int(l) for l in input().split()]
    A.append(a)
    L.append(l)
res = []
for q in range(Q):
    s, t = [int(l) for l in input().split()]
    res.append(A[s-1][t-1])
for r in res:
    print(r)
