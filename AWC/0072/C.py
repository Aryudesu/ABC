N, Q = map(int, input().split())
S = list(map(int, input().split()))
imos = [0] * (N + 1)
for _ in range(Q):
    l, r = map(int, input().split())
    imos[l-1] += 1
    imos[r] -= 1
result = []
s = 0
for idx in range(N):
    s += imos[idx]
    result.append(max(0, S[idx] - s))
print(*result)
