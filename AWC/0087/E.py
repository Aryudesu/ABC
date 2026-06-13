from atcoder.fenwicktree import FenwickTree

N, Q = map(int, input().split())
defaultAoki = 0
data = [0]
ft = FenwickTree(N)
for n in range(N):
    s, p = input().split()
    p = int(p)
    if s == "A":
        data.append(data[-1] + p)
        defaultAoki += p
        ft.add(n, p)
    else:
        data.append(data[-1] + (-p))

INF = 10 ** 18
# L <= l < r <= R があってdata[r] - data[l]が最大のものを選びたい
result = []
for _ in range(Q):
    l, r = map(int, input().split())
    if l == r:
        print(0)
        continue
    tmpMin = INF
    maxDiff = -INF
    for idx in range(l, r+1):
        tmpMin = min(tmpMin, data[idx])
        maxDiff = max(maxDiff, data[idx] - tmpMin)
    result.append(ft.sum(l-1, r) - max(0, maxDiff))
for r in result:
    print(r)
