N, K, Q = map(int, input().split())
C = list(map(int, input().split()))
imos = [0] * (N + 1)
for _ in range(Q):
    l, r = map(int, input().split())
    imos[l-1] += K
    imos[r] -= K

s = 0
result = []
for n in range(N):
    s += imos[n]
    result.append(s + C[n])
print(*result)
