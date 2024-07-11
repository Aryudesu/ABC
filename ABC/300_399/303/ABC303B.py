N, M = [int(l) for l in input().split()]
data = set()
for i in range(N-1):
    for j in range(i + 1, N):
        data.add((i + 1, j + 1))
# print(data)
for m in range(M):
    a = [int(l) for l in input().split()]
    for i in range(N - 1):
        p = (a[i], a[i+1]) if a[i] < a[i+1] else (a[i+1], a[i])
        if p in data:
            data.remove(p)
# print(data)
print(len(data))
