N, Q = map(int, input().split())
imos = [0] * (N + 1)
for _ in range(Q):
    l, r, c = map(int, input().split())
    imos[l-1] += c
    imos[r] -= c
s = 0
for i in range(N):
    s += imos[i]
    imos[i] = s
imos.pop()
print(*imos)
