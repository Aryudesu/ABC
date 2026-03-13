N, W = map(int, input().split())
INF = 10**10
bits = [1<<n for n in range(16)]
LN = []
for n in range(N):
    l, c = map(int, input().split())
    n = 0
    for i in range(16):
        if n + bits[i] >= c:
            LN.append((l * (c - n), c - n))
            break
        LN.append((l * bits[i], bits[i]))
        n += bits[i]
# print(LN)
dp = {0:0}
for l, n in LN:
    newDp = dp.copy()
    for length, num in dp.items():
        newLength = length + l
        newNum = num + n
        if newLength > W:
            continue
        if newLength not in newDp or newDp[newLength] > newNum:
            newDp[newLength] = newNum
    dp = newDp
if W in dp:
    print(dp[W])
else:
    print(-1)
