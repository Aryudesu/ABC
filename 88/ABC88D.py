def search_shortest_path(F, H, W, sh, sw, gh, gw, p_color):
    # 探索カウント
    count = 1
    # 探索するセル
    nowcell = set()
    nowcell.add(sh * W + sw)
    # 探索するセルがなくなるまで探索
    while nowcell:
        count += 1
        newcell = set()
        # セルすべて探索
        for c in nowcell:
            x = c % W
            y = c // W
            # 現在見ているセルを別の文字で置き換える
            F[y][x] = "#"
            if gh == y and gw == x:
                return count - 1
            if x + 1 < W:
                if F[y][x + 1] == p_color:
                    newcell.add(c + 1)
            if x - 1 >= 0:
                if F[y][x - 1] == p_color:
                    newcell.add(c - 1)
            if y + 1 < H:
                if F[y + 1][x] == p_color:
                    newcell.add(c + W)
            if y - 1 >= 0:
                if F[y - 1][x] == p_color:
                    newcell.add(c - W)
        nowcell = newcell
    return -1


H, W = [int(l) for l in input().split()]
S = []
wall = 0
for h in range(H):
    s = list(input())
    for t in s:
        if t == "#":
            wall += 1
    S.append(s)

res = search_shortest_path(S, H, W, 0, 0, H-1, W-1, '.')
if res > 0:
    print(H * W - res - wall)
else:
    print(-1)
