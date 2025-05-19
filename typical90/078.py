N, M = [int(l) for l in input().split()]
data = [0] * N
for m in range(M):
    a, b = [int(l) - 1 for l in input().split()]
    if a < b:
        data[b] += 1
    elif a > b:
        data[a] += 1
print(data.count(1))
