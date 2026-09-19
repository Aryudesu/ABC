N, L, R = map(int, input().split())
T = list(map(int, input().split()))
data = [1 if L <= t <= R else -1 for t in T]
S = []
INF = 10 ** 18
m = INF
s = 0
result = -INF
for idx in range(N):
    m = min(m, s)
    s += data[idx]
    result = max(result, s-m)
print(result)
