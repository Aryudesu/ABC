N, M, K = map(int, input().split())
imos = [0] * (N + 1)
L = list(map(int, input().split()))
for _ in range(M):
    x, y, z = map(int, input().split())
    imos[x-1] += z
    imos[y] -= z
s = 0
result = 0
for idx in range(N):
    s += imos[idx]
    if s + L[idx] >= K:
        result += 1
print(result)
