N, K = map(int, input().split())
data = []
for i in range(N):
    a, b = map(int, input().split())
    data.append((b - a, a))
data.sort()
result = 0
for i in range(N):
    d, a = data[i]
    result += a
    if i < K:
        result += d
print(result)
