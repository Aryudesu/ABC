from atcoder.fenwicktree import FenwickTree
N, M, K = map(int, input().split())
H = list(map(int, input().split()))
ft = FenwickTree(N)
for i in range(N):
    if H[i] >= K:
        ft.add(i, H[i])
result = 0
for l in range(N - M + 1):
    result = max(result, ft.sum(l, l + M))
print(result)
