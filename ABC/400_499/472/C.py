from atcoder.fenwicktree import FenwickTree

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
ft = FenwickTree(N)
for i in range(N):
    ft.add(i, A[i])
result = []
for r in range(N):
    l = max(0, r - M + 1)
    if ft.sum(l, r + 1) <= K:
        result.append("Yes")
    else:
        ft.add(r, -A[r])
        result.append("No")
print(*result, sep="\n")
