N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
result = []
for i in range(N):
    result.append(A[(i - K) % N])
print(*result)
