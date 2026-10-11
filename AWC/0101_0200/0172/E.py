INF = 10 ** 18
N, Q = map(int, input().split())
A = list(map(int, input().split()))
data = []
data.append((INF, -1))
idxes = []
for n in range(N):
    a = A[n]
    while data[-1][0] <= a:
        data.pop()
    idxes.append(data[-1][1] + 1)
    data.append((a, n))
imos = [0] * (N + 1)
for idx in range(N):
    l, r = idxes[idx], idx
    imos[l] += 1
    imos[r+1] -= 1
s = 0
for idx in range(N+1):
    s += imos[idx]
    imos[idx] = s
result = []
for _ in range(Q):
    l, r = map(int, input().split())
    if l == r:
        result.append(1)
        continue
    res = imos[l-1] - imos[r]
    result.append(res)
print(*result, sep="\n")
