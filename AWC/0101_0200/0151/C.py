N, Q = map(int, input().split())
AT = []
for _ in range(N):
    A, T = map(int, input().split())
    AT.append((A, T))
imos = [0] * (N + 1)
for _ in range(Q):
    l, r, x = map(int, input().split())
    imos[l-1] += x
    imos[r] -= x
s = 0
result = 0
for idx in range(N):
    s += imos[idx]
    if s + AT[idx][0] >= AT[idx][1]:
        result += 1
print(result)
