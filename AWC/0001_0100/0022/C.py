from atcoder.fenwicktree import FenwickTree

N, M, K, T = map(int, input().split())
B = list(map(int, input().split()))
ft = FenwickTree(N)
for b in B:
    ft.add(b - 1, 1)
result = []
for k in range(K):
    l, r = map(int, input().split())
    if ft.sum(l-1, r) >= T:
        result.append("YES")
    else:
        result.append("NO")
for r in result:
    print(r)
