N, M, K = [int(l) for l in input().split()]
data = [0] * N
result = []
for k in range(K):
    a, b = [int(l) for l in input().split()]
    data[a-1] += 1
    if data[a-1] == M:
        result.append(a)
print(*result)
