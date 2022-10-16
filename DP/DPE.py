N, W = [int(l) for l in input().split()]
wv = []
for n in range(N):
    wv.append([int(l) for l in input().split()])
NV = 100000
knapsack = [-1]*(NV + 1)
# 価値ごとに重さを保持
knapsack[wv[0][1]] = wv[0][0]
for n in range(1, N):
    nextk = [knapsack[k] for k in range(NV + 1)]
    for nv in range(NV + 1):
        if nextk[nv] > knapsack[nv] and knapsack[nv] != -1:
            nextk[nv] = knapsack[nv]
        if knapsack[nv] == 0 and nv > 0:
            continue
        nnv = nv + wv[n][1]
        nnw = (0 if knapsack[nv] == -1 else knapsack[nv]) + wv[n][0]
        if nnv < NV:
            continue
        if nnw > W:
            continue
        if nextk[nnv] > nnw or nextk[nnv] == -1:
            nextk[nnv] = nnw
    knapsack = nextk
    print(knapsack)
res = 0
for k in range(NV + 1):
    if knapsack[k]:
        res = k
print(res)
