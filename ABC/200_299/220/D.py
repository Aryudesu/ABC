N = int(input())
A = [int(l) for l in input().split()]
dp = [0] * 10
dp[(A[0] + A[1]) % 10] += 1
dp[(A[0] * A[1]) % 10] += 1
for i in range(2, N):
    new_dp = [0] * 10
    for j in range(10):
        new_dp[(A[i] + j) % 10] += dp[j]
        new_dp[(A[i] * j) % 10] += dp[j]
    dp = new_dp
for d in dp:
    print(d)
