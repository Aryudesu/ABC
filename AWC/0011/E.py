N, M = map(int, input().split())
dp = {0: (0, 0)}
for n in range(N):
    a, b = map(int, input().split())
    newdp = dp.copy()
    for w in dp:
        v, mask = dp[w]
        newW = w + a
        newV = v + b
        newMask = mask | (1 << n)
        if newW > M:
            continue
        if newW in newdp:
            nextV, nextMask = newdp[newW]
            if nextV == newV:
                newMask |= nextMask
            elif nextV > newV:
                continue
        newdp[newW] = (newV, newMask)
    dp = newdp

bestMask = 0
maxValue = 0
for w in dp:
    if w > M:
        continue
    val, mask = dp[w]
    if val == maxValue:
        bestMask |= mask
    elif val > maxValue:
        maxValue = val
        bestMask = mask

for i in range(N):
    print("Yes" if bestMask & (1 << i) else "No")
