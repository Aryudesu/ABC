INF = 10 ** 10

N, S, T = map(int, input().split())
# (個数, 利益): 重量
dp = {(0, 0): 0}
# 個数が答え
result = INF
for n in range(N):
    p, c, w = map(int, input().split())
    if p - c <= 0:
        continue
    nextDP = dict()
    for key in dp:
        num, val = key
        weight = dp[key]
        if result <= num:
            continue
        nextDP[key] = min(nextDP.get(key, INF), weight)
        nextNum = num + 1
        nextVal = val + p - c
        nextWeight = weight + w
        if result <= nextNum:
            continue
        if nextWeight > S:
            continue
        if nextVal >= T:
            result = min(result, nextNum)
            continue
        nextKey = (nextNum, nextVal)
        if nextKey not in nextDP or nextDP[nextKey] > nextWeight:
            nextDP[nextKey] = nextWeight
    dp = nextDP
    # print(dp)
print(-1 if result >= INF else result)
