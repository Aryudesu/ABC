N, M = map(int, input().split())
A = list(map(int, input().split()))
imos = [0] * (N + 1)
for m in range(M):
    l, r, d = map(int, input().split())
    imos[l-1] += d
    imos[r] -= d
result = []
s = 0
for i in range(N):
    s += imos[i]
    result.append(s + A[i])
print(*result)
