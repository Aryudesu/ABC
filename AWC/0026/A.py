N, K = map(int, input().split())
A = list(map(int, input().split()))
result = []
for idx in range(N):
    if (idx+1) % K == 0:
        result.append(A[idx])
print(*result)
