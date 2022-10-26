N, W = [int(l) for l in input().split()]
wv = []
for n in range(N):
    wv.append([int(l) for l in input().split()])
knapsack = dict()
# 価値ごとに重さを保持
knapsack[wv[0][1]] = wv[0][0]
for n in range(1, N):
    nextk = dict()
    for k, v in knapsack.items():
        nk = k + wv[0][0]
        nextk[k] = v + wv[0][1]
    knapsack = nextk
    print(knapsack)
res = 0
for k in range(NV + 1):
    if knapsack[k]:
        res = k
print(res)
