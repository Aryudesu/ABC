N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
for idx in range(K):
    b, c = B[idx], C[idx]
    A[b-1] = c
result = 0
for idx in range(N-1):
    result += abs(A[idx] - A[idx+1])
print(result)
