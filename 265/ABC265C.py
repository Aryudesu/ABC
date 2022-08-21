def calc(H, W, G):
    x = 0
    y = 0
    while True:
        if G[y][x] == 'D':
            if y + 1 == H:
                return x, y
            else:
                G[y][x] = '-'
                y += 1
        elif G[y][x] == 'U':
            if y - 1 == -1:
                return x, y
            else:
                G[y][x] = '-'
                y -= 1
        elif G[y][x] == 'R':
            if x + 1 == W:
                return x, y
            else:
                G[y][x] = '-'
                x += 1
        elif G[y][x] == 'L':
            if x - 1 == -1:
                return x, y
            else:
                G[y][x] = '-'
                x -= 1
        elif G[y][x] == '-':
            return None, None



H, W = [int(l) for l in input().split()]
G = []
for h in range(H):
    G.append(list(input()))


x, y = calc(H, W, G)
if x is None:
    print(-1)
else:
    print(y + 1, x + 1)
