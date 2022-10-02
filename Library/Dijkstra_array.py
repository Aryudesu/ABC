def search_shortest_path(F, H, W, sh, sw, gh, gw, p_color):
    """
    迷路を解きます
    F : 2次元配列で作成された迷路
    H : 迷路の高さ
    W : 迷路の横幅
    sh: 迷路のスタートy座標
    sw: 迷路のスタートx座標
    gh: 迷路のゴールy座標
    gw: 迷路のゴールx座標
    p_color: 迷路の通れる箇所
    """
    path = [[-1 for _ in range(W)] for _ in range(H)]
    # 探索カウント
    count = 1
    # 探索するセル
    nowcell = set()
    nowcell.add(sh * W + sw)
    # 探索するセルがなくなるまで探索
    while nowcell:
        newcell = set()
        # セルすべて探索
        for c in nowcell:
            x = c % W
            y = c // W
            # 現在見ているセルを別の文字で置き換える
            path[y][x] = count
            if gh == y and gw == x:
                break
            if x + 1 < W:
                if F[y][x + 1] == p_color and path[y][x + 1] == -1:
                    newcell.add(c + 1)
            if x - 1 >= 0:
                if F[y][x - 1] == p_color and path[y][x - 1] == -1:
                    newcell.add(c - 1)
            if y + 1 < H:
                if F[y + 1][x] == p_color and path[y + 1][x] == -1:
                    newcell.add(c + W)
            if y - 1 >= 0:
                if F[y - 1][x] == p_color and path[y - 1][x] == -1:
                    newcell.add(c - W)
        count += 1
        nowcell = newcell
    res = [[False for _ in range(W)] for _ in range(H)]
    plen = path[gh][gw]
    x = gw
    y = gh
    nx = x
    ny = y
    for p in range(plen + 1):
        res[y][x] = True
        if x + 1 < W:
            if path[y][x + 1] == plen - p:
                ny = y
                nx = x + 1
        if x - 1 >= 0:
            if path[y][x - 1] == plen - p:
                ny = y
                nx = x - 1
        if y + 1 < H:
            if path[y + 1][x] == plen - p:
                ny = y + 1
                nx = x
        if y - 1 >= 0:
            if path[y - 1][x] == plen - p:
                ny = y - 1
                nx = x
        x = nx
        y = ny
    return res, count - 1


F = [
    ['_', '_', '#', '_', '_', '_', '_', '_', '_', '_'],
    ['#', '_', '_', '_', '#', '_', '#', '_', '#', '_'],
    ['_', '_', '#', '_', '#', '_', '#', '_', '#', '_'],
    ['_', '#', '_', '_', '#', '_', '#', '_', '#', '_'],
    ['_', '#', '_', '#', '#', '_', '#', '_', '#', '_'],
    ['#', '#', '_', '#', '#', '#', '#', '#', '#', '_'],
    ['_', '_', '#', '_', '_', '_', '_', '_', '#', '_'],
    ['#', '_', '#', '_', '#', '#', '#', '_', '#', '_'],
    ['#', '_', '#', '_', '_', '_', '#', '_', '#', '_'],
    ['_', '_', '_', '_', '#', '#', '#', '_', '_', '_']
]

H = len(F)
W = len(F[0])

res, count = search_shortest_path(F, H, W, 0, 0, 6, 0, '_')
print('元迷路')
for h in range(H):
    mes = ""
    for w in range(W):
        if F[h][w] == '#':
            mes += "[#]"
        elif F[h][w] == '_':
            if h == 0 and w == 0:
                mes += "[S]"
            elif h == 6 and w == 0:
                mes += "[G]"
            else:
                mes += "[ ]"
    print(mes)
print("結果")
for h in range(H):
    mes = ""
    for w in range(W):
        if F[h][w] == '#':
            mes += "[#]"
        elif F[h][w] == '_':
            if res[h][w]:
                if h == 0 and w == 0:
                    mes += "[S]"
                elif h == 6 and w == 0:
                    mes += "[G]"
                else:
                    mes += "[ ]"
            else:
                mes += "[=]"
    print(mes)
