def calc(H, W, D, y1, x1, y2, x2, S):
    c = 0
    for h in range(H):
        for w in range(W):
            if ((abs(y1 - h) + abs(x1 - w)) <= D or (abs(y2 - h) + abs(x2 - w)) <= D) and S[h][w] == ".":
                c += 1
    return c



H, W, D = [int(l) for l in input().split()]
S = []
for h in range(H):
    S.append(input())
pos = []
for h in range(H):
    for w in range(W):
        if S[h][w] == ".":
            pos.append((h, w))
result = 0
for i in range(1, len(pos)):
    for j in range(i):
        y1, x1 = pos[i]
        y2, x2 = pos[j]
        tmp = calc(H, W, D, y1, x1, y2, x2, S)
        if result < tmp:
            result = tmp
print(result)
