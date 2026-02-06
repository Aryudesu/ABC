N, M = map(int, input().split())
data = [0] * N
for m in range(M):
    a, b = map(int, input().split())
    data[a-1] += 1
    data[b-1] += 1
# print(data)
result = []
for i in range(N):
    tmp = N - data[i] - 1
    if tmp >= 3:
        result.append((tmp * (tmp - 1) * (tmp - 2)) // 6)
    else:
        result.append(0)
print(*result)
