N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
data = [False] * (N + 1)
for a in A:
    if a <= N:
        data[a] = True
result = 0
for n in range(N + 1):
    if data[n] == False:
        result = n
        break
print(result)
