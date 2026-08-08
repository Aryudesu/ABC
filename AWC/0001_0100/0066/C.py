N, Q = map(int, input().split())
W = list(map(int, input().split()))
imos = [0] * (N + 1)
for _ in range(Q):
    l, r, d = map(int, input().split())
    imos[l-1] += d
    imos[r] -= d
result = 0
s = 0
for i in range(N):
    s += imos[i]
    if W[i] - s <= 0:
        result += 1
print(result)
