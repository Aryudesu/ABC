def calcW(W, y, S, K, Ma):
    dCount = 0
    xCount = 0
    oCount = 0
    result = Ma
    for k in range(K):
        if S[y][k] == "o":
            oCount += 1
        elif S[y][k] == "x":
            xCount += 1
        else:
            dCount += 1
    if xCount == 0:
        result = min(result, dCount)
    for dx in range(W - K):
        if S[y][dx] == "o":
            oCount -= 1
        elif S[y][dx] == "x":
            xCount -= 1
        else:
            dCount -= 1
        if S[y][dx + K] == "o":
            oCount += 1
        elif S[y][dx + K] == "x":
            xCount += 1
        else:
            dCount += 1
        if xCount == 0:
            result = min(result, dCount)
    return result

def calcH(H, x, S, K, Ma):
    dCount = 0
    xCount = 0
    oCount = 0
    result = Ma
    for k in range(K):
        if S[k][x] == "o":
            oCount += 1
        elif S[k][x] == "x":
            xCount += 1
        else:
            dCount += 1
    if xCount == 0:
        result = min(result, dCount)
    for dy in range(H - K):
        if S[dy][x] == "o":
            oCount -= 1
        elif S[dy][x] == "x":
            xCount -= 1
        else:
            dCount -= 1
        if S[dy + K][x] == "o":
            oCount += 1
        elif S[dy + K][x] == "x":
            xCount += 1
        else:
            dCount += 1
        if xCount == 0:
            result = min(result, dCount)
    return result

def calc(H, W, S, K):
    result = H + W
    if K <= W:
        for y in range(H):
            tmp = calcW(W, y, S, K, H + W)
            result = min(tmp, result)
    if K <= H:
        for x in range(W):
            tmp = calcH(H, x, S, K, H + W)
            result = min(tmp, result)
    return -1 if result == H + K else result



H, W, K = [int(l) for l in input().split()]
S = []
for h in range(H):
    S.append(input())
print(calc(H, W, S, K))

