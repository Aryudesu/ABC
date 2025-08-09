INF = 10 ** 18
N = int(input())
H = [int(l) for l in input().split()]
data = [(INF, None)] * N
data[0] = (0, None)
for idx in range(N):
    now_h = H[idx]
    h, p = data[idx]
    for k in range(1, 3):
        if idx + k < N:
            dh, po = data[idx + k]
            if h + abs(now_h - H[idx + k]) < dh:
                data[idx + k] = (h + abs(now_h - H[idx + k]), idx)
result = []
idx = N-1
while not idx is None:
    result.append(idx + 1)
    idx = data[idx][1]
result.reverse()
print(len(result))
print(*result)
