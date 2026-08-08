N, M = map(int, input().split())
imos = [0] * (N + 1)
for m in range(M):
    l, r = map(int, input().split())
    imos[l-1] += 1
    imos[r] -= 1

s = 0
for i in range(N):
    s += imos[i]
    imos[i] = s
imos.pop()
print(*imos)
