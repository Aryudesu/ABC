N = int(input())
A = [int(l) for l in input().split()]
A.sort()
result = None
for i in range(N-1):
    if A[i] + 1 != A[i+1]:
        result = A[i] + 1
print(result)
