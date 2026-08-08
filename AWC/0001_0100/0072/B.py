from atcoder.fenwicktree import FenwickTree

N, K = map(int, input().split())
A = list(map(int, input().split()))
allSum = sum(a for a in A if a >= 0)
data = [min(0, a) for a in A]
ft = FenwickTree(N)
for idx in range(N):
    ft.add(idx, data[idx])
result = -10**18
for l in range(N-K+1):
    r = l + K - 1
    res = ft.sum(l, r + 1)
    result = max(res, result)

print(allSum + result)
