N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
result = (A[0] + A[1]) * (K // 2)
if K % 2:
    result += A[0]
print(result)
