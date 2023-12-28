N, W = [int(l) for l in input().split()]
WV = []
for n in range(N):
    w, v = [int(l) for l in input().split()]
    WV.append((w, v))

dp = {0: 0}
for wv in WV:
    w, v = wv
    new_dp = {w: v}
    for w1 in dp:
        if new_dp.get(w1, 0) < dp.get(w1, 0):
            new_dp[w1] = dp.get(w, 0)
        if w1 + w > W:
            continue
        v1 = dp.get(w1, 0)
        if new_dp.get(w1 + w, 0) < v1 + v:
            new_dp[w1 + w] = v1 + v
    dp = new_dp
    print(dp)
