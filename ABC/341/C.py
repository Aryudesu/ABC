H, W, N = [int(l) for l in input().split()]
T = input()
field = [input() for _ in range(H)]
data = []
for y in range(H):
    data.append([-1] * W)
result = 0
for y in range(1, H - 1):
    for x in range(1, W - 1):
        py, px = y, x
        f = True
        # 不時着位置が海はスルー
        if field[py][px] == "#":
            continue
        for i in range(0, N):
            # 1回移動
            if T[i] == "D":
                py += 1
            elif T[i] == "U":
                py -= 1
            elif T[i] == "L":
                px -= 1
            elif T[i] == "R":
                px += 1
            if field[py][px] == "#":
                f = False
                break
        if f:
            result += 1
print(result)
