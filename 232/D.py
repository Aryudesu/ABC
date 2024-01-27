H, W = [int(l) for l in input().split()]
C = [input() for _ in range(H)]
dp = set([(0, 0)])
count = 0
while dp:
    new_dp = set()
    for y, x in dp:
        if 0 <= y + 1 < H and C[y + 1][x] != "#":new_dp.add((y + 1, x))
        if 0 <= x + 1 < W and C[y][x + 1] != "#":new_dp.add((y, x + 1))
    dp, count = new_dp, count + 1
print(count)
