N = int(input())
P = [-1] + [int(l) - 1 for l in input().split()]
V = list(map(int, input().split()))
dp = [0] * N
isOk = True
for idx in range(N - 1, 0, -1):
    if V[idx] < dp[idx]:
        isOk = False
        break
    dp[P[idx]] += V[idx]
if V[0] < dp[0]:
    isOk = False
print("Yes" if isOk else "No")
