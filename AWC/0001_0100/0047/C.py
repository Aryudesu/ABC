from atcoder.fenwicktree import FenwickTree
N, Q = map(int, input().split())
A = list(map(int, input().split()))
ft = FenwickTree(N+1)

result = []
for _ in range(Q):
    n, *query = list(map(int, input().split()))
    if n == 1:
        l, r, x = query
        ft.add(l-1, x)
        ft.add(r, -x)
    elif n == 2:
        p = query[0]
        result.append(ft.sum(0, p) + A[p-1])
    else:
        raise ValueError()
for r in result:
    print(r)
