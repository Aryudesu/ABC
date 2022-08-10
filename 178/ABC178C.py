N = int(input())
MOD = 10**9 + 7
# [1-8, 0, 9, 0-9]の場合分け
prev = [8, 1, 1, 0]
for n in range(1, N):
    now = [0, 0, 0, 0]
    # 1-8に1-8追加
    now[0] = (prev[0] * 8) % MOD
    # 0付きに1-8追加するか1-8に0を追加
    now[1] = (prev[1] * 9 + prev[0]) % MOD
    # 9付きに1-8追加するか1-8に9追加
    now[2] = (prev[2] * 9 + prev[0]) % MOD
    # 0付きに9追加か9付きに0追加か09付きに0-9追加
    now[3] = (prev[1] + prev[2] + prev[3] * 10) % MOD
    prev = now
print(prev[3])
