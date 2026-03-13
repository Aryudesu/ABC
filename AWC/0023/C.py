from atcoder.fenwicktree import FenwickTree

N, M = map(int, input().split())
ft = FenwickTree(N)
T = list(map(int, input().split()))
for idx in range(N):
    ft.add(idx, T[idx])
result = []
for m in range(M):
    s, l, r = map(int, input().split())
    result.append(s + ft.sum(l-1, r))
for r in result:
    print(r)
