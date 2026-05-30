N, S, T = map(int, input().split())
M = S - T
data = [0] * (M + 1)
for n in range(N):
    c, v = map(int, input().split())
    for i in range(M, -1, -1):
        if c + i > M:
            continue
        data[c + i] = max(data[c + i], data[i] + v)
print(max(data))
