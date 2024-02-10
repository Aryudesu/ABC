H, W, N = [int(l) for l in input().split()]
field = [["."]*W for _ in range(H)]
tx, ty = (0, 0)
dx, dy = (0, -1)
for _ in range(N):
    if field[ty][tx] == ".":
        dx, dy = -dy, dx
        field[ty][tx] = "#"
    else:
        dx, dy = dy, -dx
        field[ty][tx] = "."
    tx = (tx + dx) % W
    ty = (ty + dy) % H
for f in field:
    print("".join(f))
