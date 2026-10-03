N = int(input())
A = list(map(int, input().split()))
result = 0
for n in range(1, N-1):
    result += A[n-1] < A[n] > A[n+1]
print(result)
