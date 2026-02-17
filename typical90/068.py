from atcoder.dsu import DSU
from atcoder.fenwicktree import FenwickTree

N = int(input())
Q = int(input())
dsu = DSU(N + 1)
ft = FenwickTree(N + 1)
data = [None] * (N + 1)
result = []
for _ in range(Q):
    t, x, y, v = map(int, input().split())
    if t == 0:
        sgn = 1 if x % 2 == 0 else -1
        data[x] = sgn * v
        ft.add(x, sgn * v)
        dsu.merge(x, y)
    elif t == 1:
        if not dsu.same(x, y):
            result.append("Ambiguous")
            continue
        n = (max(x, y) - min(x, y))
        #  A[X] + A[X + 奇数(nとする)] = V[i] - V[i+1] + V[i+2] - ... + V[i + (n-1)]
        #  A[X] - A[X + 偶数(nとする)] = V[i] - V[i+1] + V[i+2] - ... - V[i + (n-1)]
        # X < Yのとき
        #  A[Y = X + 奇数(nとする)] = V[X] - V[X+1] + V[X+2] - ... + V[Y-1] - A[X]
        # -A[Y = X + 偶数(nとする)] = V[X] - V[X+1] + V[X+2] - ... - V[Y-1] + A[X]
        # X > Yのとき
        #  A[X] = V[X] - V[X+1] + V[X+2] - ... + V[Y-1] - A[Y = X + 奇数(nとする)]
        #  A[X] = V[X] - V[X+1] + V[X+2] - ... - V[Y-1] + A[Y = X + 偶数(nとする)]
        if x < y:
            if n % 2:
                s = ft.sum(x, y) - v
                if data[x] is None:
                    raise Exception()
                if data[x] > 1:
                    pass
    else:
        raise ValueError()
for r in result:
    print(r)
