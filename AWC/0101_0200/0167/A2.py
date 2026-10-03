N = int(input())
A = list(map(int, input().split()))
print(sum(A[n-1] < A[n] > A[n+1] for n in range(1, N-1)))
