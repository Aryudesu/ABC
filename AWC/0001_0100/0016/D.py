from atcoder.fenwicktree import FenwickTree

N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
sumDat = [0]
for a in A:
    sumDat.append(sumDat[-1] + a)
# print(sumDat)
data = []
r = 0
for l in range(N):
    while r < N and sumDat[r] - sumDat[l] <= K:
        r += 1
    if r >= N:
        data.append(N)
    else:
        data.append(r)
ft = FenwickTree(N)
for i in range(N):
    ft.add(i, data[i])
result = []
for _ in range(Q):
    l, r = map(int, input().split())
    result.append(ft.sum(l-1, r))
for r in result:
    print(r)
