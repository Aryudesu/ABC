N, W = [int(l) for l in input().split()]
WV = []
for n in range(N):
    WV.append([int(l) for l in input().split()])
# 価値をキーにして重さを値にする
knapsack = {0: 0}
for wv in WV:
    new_knapsack = dict()
    for k in knapsack:
        if new_knapsack.get(k, W + 1) >= knapsack[k]:
            new_knapsack[k] = knapsack[k]
        w = knapsack.get(k)
        if w + wv[0] <= W:
            n_w = new_knapsack.get(k + wv[1], W + 1)
            if n_w > w + wv[0]:
                new_knapsack[k + wv[1]] = w + wv[0]
    knapsack = new_knapsack
result = 0
for k in knapsack:
    if k > result:
        result = k
print(result)
