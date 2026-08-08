N = int(input())
A = list(map(int, input().split()))
result = max(A[0] + A[1], A[-1] + A[-2])
for i in range(1, N-1):
    result = max(A[i-1] + A[i] + A[i + 1], result)
print(result)
