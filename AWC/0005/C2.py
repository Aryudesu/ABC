N, K = map(int, input().split())
A = list(map(int, input().split()))
L = [0] * N
R = [0] * N
L[0] = A[0]
R[-1] = A[-1]
for i in range(N - 1):
    L[i+1] = max(A[i+1], L[i] - K)
    R[N-2-i] = max(A[N-2-i], R[N-1-i] - K)
result = 0
for i in range(N):
    result += max(L[i], R[i]) - A[i]
print(result)
