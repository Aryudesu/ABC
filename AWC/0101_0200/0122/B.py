N, D = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
result1 = 0
for n in range(N-1):
    diff = A[n+1] - A[n]
    if diff > D:
        result1 += diff
result2 = 0
for n in range(N-1):
    diff = A[-n-1] - A[-1-n-1]
    if diff > D:
        result2 += diff
print(min(result1, result2))
