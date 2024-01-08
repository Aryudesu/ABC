from atcoder.fenwicktree import FenwickTree

N = int(input())
ft0, ft1 = FenwickTree(N), FenwickTree(N)
for n in range(N):
    c, p = [int(l) for l in input().split()]
    ft0.add(n, p) if c == 1 else ft1.add(n, p)
for _ in range(int(input())):
    l, r = [int(l) for l in input().split()]
    print(ft0.sum(l - 1, r), ft1.sum(l - 1, r))
