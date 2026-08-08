
N, K = map(int, input().split())
# c[(k, 選んだかどうか)] = v
dp = dict()
dp[(0, False)] = 0
for n in range(N):
    v, w = map(int, input().split())
    nextDP = dict()
    for key in dp:
        weight, choise = key
        value = dp[key]
        # 前を選ばなかった場合
        if not choise:
            # 選ぶ場合
            if weight + w <= K:
                nextKey = (weight + w, True)
                nextDP[nextKey] = max(nextDP.get(nextKey, 0), value + v)
        # 選ばない場合
        nextKey = (weight, False)
        nextDP[nextKey] = max(nextDP.get(nextKey, 0), value)
    dp = nextDP
result = 0
for key, value in dp.items():
    result = max(result, value)
print(result)
