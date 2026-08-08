N, M, K = map(int, input().split())

AB = []
for n in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))
# dp[どこの町][宿泊費] = 最大稼ぎ
dp = [[0] * (M + 1) for _ in range(N)]
for i in range(N):
    a, b = AB[i]
    dp[i][b] = a
for d in dp:
    print(d)

for n in range(1, N + 1):
    nextDP = [[0] * (M + 1) for _ in range(N)]
    for k in range(1, K + 1):
        p = n - k
        if p < 0:
            break
        for m in range(M):
            pass
