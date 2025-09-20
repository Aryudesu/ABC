def calc(H, W, field):
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for h in range(H):
        for w in range(W):
            if field[h][w] != "#":
                continue
            count = 0
            for dh, dw in d:
                if h + dh >= H or h + dh < 0:
                    continue
                if w + dw >= W or w + dw < 0:
                    continue
                if field[h + dh][w + dw] == "#":
                    count += 1
            if count != 2 and count != 4:
                return False
    return True
                

H, W = [int(l) for l in input().split()]
field = [input() for _ in range(H)]
print("Yes" if calc(H, W, field) else "No")
