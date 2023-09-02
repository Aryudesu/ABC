def get_level(C, y, x, H, W):
    r = 0
    while True:
        if y + r < H and y - r >= 0 and x + r < W and x - r >= 0:
            pass
        else:
            break
        if C[y + r][x + r] and C[y + r][x - r] and C[y - r][x + r] and C[y - r][x - r]:
            r += 1
        else:
            break
    return r - 1 if r - 1 > 0 else 0


H, W = [int(l) for l in input().split()]
C = [[True if l == "#" else False for l in input()] for _ in range(H)]
result = [0] * min([H, W])
for y in range(H):
    for x in range(W):
        tmp = get_level(C, y, x, H, W)
        if tmp:
            result[tmp - 1] += 1
print(*result)
