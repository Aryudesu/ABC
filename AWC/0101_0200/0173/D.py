N, M = map(int, input().split())
H = list(map(int, input().split()))
imos = [0] * (M + 1)
for _ in range(N):
    l, r, a = map(int, input().split())
    imos[l-1] += a
    imos[r] -= a

s = 0
result = 0
for m in range(M):
    s += imos[m]
    result += H[m] <= s
print(result)
