N, W = [int(l) for l in input().split()]
WV = []
for n in range(N):
    WV.append([int(l) for l in input().split()])
# [W: V]でいく？
dp = dict()
dp[0] = 0
result = 0
for wv in WV:
    w, v = wv
    new_dp = dict()
    for kw in dp:
        if dp.get(kw, 0) >= new_dp.get(kw, 0):
            new_dp[kw] = dp.get(kw, 0)
        nv = v + dp.get(kw, 0)
        if w + kw <= W:
            if new_dp.get(w + kw, 0) < nv:
                if result < nv:
                    result = nv
                new_dp[w + kw] = nv
    dp = new_dp
    # print(dp)
print(result)
