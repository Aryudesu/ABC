N, W = [int(l) for l in input().split()]
WV = []
for n in range(N):
    WV.append([int(l) for l in input().split()])
# 重さをキーにする
knapsack = {0: 0}
for wv in WV:
    new_knapsack = dict()
    for k in knapsack:
        if new_knapsack.get(k, 0) <= knapsack[k]:
            new_knapsack[k] = knapsack[k]
        if k + wv[0] <= W:
            val = knapsack[k]
            n_val = new_knapsack.get(k + wv[0], 0)
            if n_val < val + wv[1]:
                new_knapsack[k + wv[0]] = val + wv[1]
    knapsack = new_knapsack
result = 0
for k in knapsack:
    if result < knapsack[k]:
        result = knapsack[k]
print(result)
