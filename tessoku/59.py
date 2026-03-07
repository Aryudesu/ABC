from atcoder.fenwicktree import FenwickTree

N, Q = map(int, input().split())
ft = FenwickTree(N)
for _ in range(Q):
    n, a, b = map(int, input().split())
    if n == 1:
        ft.add(a-1, b - ft.sum(a-1, a))
    else:
        print(ft.sum(a-1, b-1))
