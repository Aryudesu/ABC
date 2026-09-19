N, M, K = map(int, input().split())
A = list(map(int, input().split()))
imos = [0] * (N + 1)
for m in range(M):
    l, r = map(int, input().split())
    imos[l-1] += 1
    imos[r] -= 1
s = 0
result = 0
for idx in range(N):
    s += imos[idx]
    result += s + A[idx] >= K
print(result)
