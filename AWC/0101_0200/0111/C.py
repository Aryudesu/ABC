N, M = map(int, input().split())
H = list(map(int, input().split()))
T = list(map(int, input().split()))
imos = [0] * (N + 1)
for m in range(M):
    l, r, w = map(int, input().split())
    imos[l-1] += w
    imos[r] -= w
result = 0
s = 0
for idx in range(N):
    s += imos[idx]
    if H[idx] + s >= T[idx]:
        result += 1
print(result)
