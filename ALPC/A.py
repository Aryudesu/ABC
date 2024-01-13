from atcoder.dsu import DSU

# 呼び出し
N, Q = [int(l) for l in input().split()]

uf = DSU(N)
res = []
for q in range(Q):
    t, u, v = [int(l) for l in input().split()]
    if t:
        res.append(1 if uf.same(u, v) else 0)
    else:
        uf.merge(u, v)
for r in res:
    print(r)
