N, K = map(int, input().split())
T = list(map(int, input().split()))
imos = [0] * (N + 1)
s = 0
for i in range(N - K + 1):
    s += imos[i]
    d = T[i] - s
    imos[i] += d
    s += d
    imos[i + K] -= d
isOk = True
s = 0
for i in range(N):
    s += imos[i]
    if s != T[i]:
        isOk = False
        break
print("Yes" if isOk else "No")
