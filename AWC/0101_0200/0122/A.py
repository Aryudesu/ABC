N, M = map(int, input().split())
data = [False] * N
data[0] = True
for m in range(M):
    a, b = map(int, input().split())
    if data[a]:
        data[b] = True
print(sum(data))
