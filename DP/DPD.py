N, W = [int(l) for l in input().split()]
wv = []
for n in range(N):
    wv.append([int(l) for l in input().split()])
knapsack = [[0]*(W + 1) for _ in range(N)]
knapsack[0][wv[0][0]] = wv[0][1]
for n in range(1, N):
    for w in range(W + 1):
        if knapsack[n-1][w] > knapsack[n][w]:
            knapsack[n][w] = knapsack[n-1][w]
        if knapsack[n - 1][w] == 0 and w > 0:
            continue
        nw = w + wv[n][0]
        if nw > W:
            continue
        if knapsack[n][nw] < knapsack[n-1][w] + wv[n][1]:
            knapsack[n][nw] = knapsack[n-1][w] + wv[n][1]
print(max(knapsack[-1]))
