def search_shortest_path(F, H, W, sh, sw, p_color):
    # 探索するセル
    path = [[-1 for _ in range(W)] for _ in range(H)]
    # 探索カウント
    count = 1
    # 探索するセル
    nowcell = set()
    B = W
    if B < 4:
        B = 4
    # 最初に進んだ方向に符号をつける
    if sh - 1 >= 0:
        if F[sh - 1][sw] == p_color:
            nowcell.add((sh-1) * B * B + sw * B + 0)
    if sh + 1 < H:
        if F[sh + 1][sw] == p_color:
            nowcell.add((sh+1) * B * B + sw * B + 1)
    if sw - 1 >= 0:
        if F[sh][sw - 1] == p_color:
            nowcell.add(sh * B * B + (sw-1) * B + 2)
    if sw + 1 < W:
        if F[sh][sw + 1] == p_color:
            nowcell.add(sh * B * B + (sw+1) * B + 3)
    # 探索するセルがなくなるまで探索
    while nowcell:
        newcell = set()
        # セルすべて探索
        for c in nowcell:
            # 現在位置
            x = (c % (B * B))//B
            y = c // (B*B)
            # 符号
            k = c % B
            if y - 1 >= 0:
                if F[y - 1][x] == p_color:
                    for m in range(4):
                        if m == k:
                            continue
                        if (y-1) * B * B + x * B + m in newcell:
                            return True
            if y + 1 < H:
                if F[y + 1][x] == p_color:
                    for m in range(4):
                        if m == k:
                            continue
                        if (y+1) * B * B + x * B + m in newcell:
                            return True
            if x - 1 >= 0:
                if F[y][x - 1] == p_color:
                    for m in range(4):
                        if m == k:
                            continue
                        if y * B * B + (x-1) * B + m in newcell:
                            return True
            if x + 1 < W:
                if F[y][x + 1] == p_color:
                    for m in range(4):
                        if m == k:
                            continue
                        if y * B * B + (x+1) * B + m in newcell:
                            return True
            # 現在見ているセルを別の文字で置き換える
            path[y][x] = count
            if x + 1 < W:
                if F[y][x + 1] == p_color and path[y][x + 1] == -1:
                    newcell.add(y * B * B + (x+1) * B + k)
            if x - 1 >= 0:
                if F[y][x - 1] == p_color and path[y][x - 1] == -1:
                    newcell.add(y * B * B + (x-1) * B + k)
            if y + 1 < H:
                if F[y + 1][x] == p_color and path[y + 1][x] == -1:
                    newcell.add((y+1) * B * B + x * B + k)
            if y - 1 >= 0:
                if F[y - 1][x] == p_color and path[y - 1][x] == -1:
                    newcell.add((y-1) * B * B + x * B + k)
        count += 1
        nowcell = newcell
    return False


H, W = [int(l) for l in input().split()]
C = []
sh = 0
sw = 0
for h in range(H):
    c = input()
    for w in range(W):
        if c[w] == "S":
            sh = h
            sw = w
            break
    C.append(c)
print('Yes' if search_shortest_path(C, H, W, sh, sw, ".") else 'No')
