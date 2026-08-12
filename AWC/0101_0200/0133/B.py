N, K, T = map(int, input().split())
A = list(map(int, input().split()))
result = A[T-1]
A[T-1] = -1
A.sort()
for k in range(K-1):
    a = A.pop()
    result += a
print(result)
