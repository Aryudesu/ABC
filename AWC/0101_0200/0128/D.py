N, M, T = map(int, input().split())
F = list(map(int, input().split()))
imos = [0] * (N + 1)
for m in range(M):
    l, r, d = map(int, input().split())
    imos[l-1] += d
    imos[r] -= d
s = 0
result = 0
for idx in range(N):
    s += imos[idx]
    result += F[idx] - s <= T
print(result)
