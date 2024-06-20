N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
data = [0] * M
for n in range(N):
    X = [int(l) for l in input().split()]
    for idx in range(M):
        data[idx] += X[idx]
result = True
for idx in range(M):
    if A[idx] > data[idx]:
        result = False
        break
print("Yes" if result else "No")
