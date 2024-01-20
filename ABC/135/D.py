S = input()
L_MOD = 13
MOD = 10**9 + 7
dp = dict()
s = S[0]
if s == "?":
    for i in range(10):
        dp[i] = 1
else:
    dp[int(s)] = 1
for idx in range(1, len(S)):
    s = S[idx]
    new_dp = dict()
    # ワイルドカードの場合
    if s == "?":
        for i in range(10):
            for k in range(13):
                key = (i + k * 10) % L_MOD
                new_dp[key] = (new_dp.get(key, 0) + dp.get(k, 0)) % MOD
    # 数値の場合
    else:
        for k in range(13):
            key = (int(s) + k * 10) % L_MOD
            new_dp[key] = (new_dp.get(key, 0) + dp.get(k, 0)) % MOD
    dp = new_dp
print(dp.get(5, 0))
