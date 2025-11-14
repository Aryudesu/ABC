N, K = map(int, input().split())
A = list(map(int, input().split()))
result = 0
l = 0
for r in range(N):
    while A[r] - A[l] > K:
        l += 1
    result += r - l
print(result)
