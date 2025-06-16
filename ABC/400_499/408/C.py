N, M = [int(l) for l in input().split()]
INF = 10**9
imos = [0] * (N + 1)
data = [0] * (N + 1)
for m in range(M):
    L, R = [int(l) for l in input().split()]
    imos[L-1] += 1
    imos[R] -= 1
c = 0
for i in range(N):
    c += imos[i]
    data[i] = c
result = INF
for i in range(N):
    result = min(result, data[i])
# print(data)
print(result)
