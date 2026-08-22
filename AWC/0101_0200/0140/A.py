N = int(input())
A = list(map(int, input().split()))
result = A[0]
for i in range(1, N):
    result += A[i]
    if A[i] > A[i-1]:
        result += A[i]
print(result)
