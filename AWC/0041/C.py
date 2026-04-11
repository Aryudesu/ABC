from bisect import bisect_left

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
result = 0
for idx in range(N):
    a = A[idx]
    tmp = bisect_left(A, K-a)
    result += N - max(idx+1, tmp)
print(result)
