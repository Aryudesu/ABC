from atcoder.fenwicktree import FenwickTree
N, K, G = map(int, input().split())
S = G
ft = FenwickTree(N)
for n in range(N):
    d, t = map(int, input().split())
    ft.add(n, t)
    S += t
M = 0
for i in range(N):
    s = ft.sum(i, min(N, i + K))
    M = max(s, M)
print(S - M)
