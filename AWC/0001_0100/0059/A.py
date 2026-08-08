N = int(input())
A = list(map(int, input().split()))
for i in range(N-1):
    if A[i] is None:
        continue
    if A[i] < A[i+1]:
        A[i + 1] += A[i]//2
        A[i] = None
    elif A[i] > A[i+1]:
        A[i] += A[i + 1] // 2
        A[i + 1] = None
print(sum(a is not None for a in A ))
