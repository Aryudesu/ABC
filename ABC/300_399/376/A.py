N, C = [int(l) for l in input().split()]
T = [int(l) for l in input().split()]
s = T[0]
result = 1
for i in range(1, N):
    if T[i] - s >= C:
        result += 1
        s = T[i]
print(result)
