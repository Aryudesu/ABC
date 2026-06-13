N, M = map(int, input().split())
A = list(map(int, input().split()))
imos = [0] * (N + 1)
for m in range(M):
    l, r = map(int, input().split())
    imos[l-1] += 1
    imos[r] -= 1
result = 0
s = 0
for idx in range(N):
    s += imos[idx]
    if s:
        result += A[idx]
print(result)
