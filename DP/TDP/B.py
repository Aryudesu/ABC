X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
INF = 10**18

dp = dict()
dp[(X-1, Y-1)] = 0
turn = True
for _ in range(X + Y):
    nextDP = dict()
    for key, value in dp.items():
        x, y = key
        if x >= 0:
            newKey = (x-1, y)
            if turn:
                nextDP[newKey] = max(nextDP.get(newKey, -INF), value + A[x])
            else:
                nextDP[newKey] = min(nextDP.get(newKey, INF), value - A[x])
        if y >= 0:
            newKey = (x, y-1)
            if turn:
                nextDP[newKey] = max(nextDP.get(newKey, -INF), value + B[y])
            else:
                nextDP[newKey] = min(nextDP.get(newKey, INF), value - B[y])
    turn = not turn
    dp = nextDP
total = dp[(-1, -1)]
result = ((sum(A) + sum(B)) + total)//2
print(result)
