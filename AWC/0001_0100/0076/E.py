from atcoder.fenwicktree import FenwickTree

N, K, Q = map(int, input().split())
D = list(map(int, input().split()))
dData = []
for n in range(N):
    dData.append((D[n], n))
dData.sort(reverse=True)
TLRQ = []
for q in range(Q):
    l, r, t = map(int, input().split())
    TLRQ.append((t, l, r, q))
TLRQ.sort()

ft = FenwickTree(N + 1)
result = []
for t, l, r, q in TLRQ:
    while dData and dData[-1][0] <= t:
        d, n = dData.pop()
        ft.add(n, 1)
    res = ft.sum(l-1, r)
    result.append((q, res if res <= K else -1))
result.sort()
for _, res in result:
    print(res)
