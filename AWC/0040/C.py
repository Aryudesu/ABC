N, K = map(int, input().split())
X = list(map(int, input().split()))
X.sort()
result = 0
l = 0
for r in range(N):
    while X[r] - X[l] > K:
        l += 1
    result = max(result, r-l+1)
print(result)
