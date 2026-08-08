N = int(input())
A = list(map(int, input().split()))
count = 0
for idx in range(1, N-1):
    count += A[idx-1] < A[idx] and A[idx] > A[idx+1]
print(count)
