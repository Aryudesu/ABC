N, M, T = map(int, input().split())
ABC = []
base = 0
data = []
for n in range(N):
    a, b, c = map(int, input().split())
    # 何もしなくても残るやつ
    if b >= T:
        base += a
    else:
        data.append((a, c))
    ABC.append((a, b, c))
# 予算内のコスト -> 最大価値
dp = {0: 0}
for a, c in data:
    nextDP = dp.copy()
    for cost in dp:
        value = dp[cost]
        nextCost = cost + c
        nextValue = value + a
        if nextCost > M:
            continue
        nextDP[nextCost] = max(nextDP.get(nextCost, 0), nextValue)
    dp = nextDP
result = 0
for key in dp:
    value = dp[key]
    result = max(result, value)
print(base + result)
