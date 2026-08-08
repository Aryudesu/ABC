N = int(input())
X = list(map(int, input().split()))
X.sort()
result = -10**10
for idx in range(N-1):
    diff = X[idx+1] - X[idx]
    result = max(result, diff)
if N == 1:
    print(0)
else:
    print(result)
