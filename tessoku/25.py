H, W = [int(l) for l in input().split()]
field = [input() for _ in range(H)]
data = [[0]*W for _ in range(H)]
data[0][0] = 1

for w in range(W):
    if field[0][w] == "#":
        tmp = 0
        break
    data[0][w] = 1

for h in range(1, H):
    tmp = 0
    for w in range(W):
        if field[h][w] == "#":
            tmp = 0
            continue
        tmp += data[h-1][w]
        data[h][w] = tmp
print(data[-1][-1])
