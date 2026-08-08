N, K = map(int, input().split())
A = list(map(int, input().split()))
l = 0
k = 0
result = 0
for r in range(N):
    k += A[r]
    while k > K:
        k -= A[l]
        l += 1
    result = max(result, r - l + 1)
print(result)

