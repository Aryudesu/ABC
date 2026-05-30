from atcoder.fenwicktree import FenwickTree

N, M = map(int, input().split())
S = list(map(int, input().split()))
P = list(map(int, input().split()))
ft = FenwickTree(N)
for idx in range(N):
    ft.add(idx, S[idx] >= P[idx])
result = []
for m in range(M):
    l, r = map(int, input().split())
    sm = ft.sum(l-1, r)
    if sm >= (r - l + 1):
        result.append("Yes")
    else:
        result.append("No")
for r in result:
    print(r)
