N, V = map(int, input().split())
W = list(map(int, input().split()))
result = 0
for i in range(N):
    if i + 1 > V:
        continue
    for j in range(i+1, N):
        if i + j + 2 > V:
            continue
        for k in range(j+1, N):
            if i + j + k + 3 > V:
                continue
            result = max(result, W[i] + W[j] + W[k])
print(result)
