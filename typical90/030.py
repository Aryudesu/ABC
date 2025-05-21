def calc(N):
    result = [True] * (N + 1)
    data = [0] * (N + 1)
    for i in range(2, N + 1):
        if not result[i]:
            continue
        idx = 1
        while idx * i <= N:
            result[idx * i] = False
            data[idx * i] += 1
            idx += 1
    return data


N, K = [int(l) for l in input().split()]
data = calc(N)
count = 0
for i in range(N + 1):
    if data[i] >= K:
        count += 1
print(count)
