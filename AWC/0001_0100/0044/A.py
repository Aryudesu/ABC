N, M = map(int, input().split())
now = M
data = [0] * N
for n in range(N):
    c, s = map(int, input().split())
    dt = min(now, c - s)
    now = now - dt
    data[n] = s + dt
for r in data:
    print(r)
