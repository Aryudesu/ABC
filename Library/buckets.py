def buckets(F, H, W, sh, sw, p_color, a_color):
    '''
    ペイントバケツの要領で置換を行います
    F : 2次元配列の地図情報
    H : 地図の高さ
    W : 地図の横幅
    h : 探索スタート地点y座標
    w : 探索スタート地点x座標
    p_color : 置換対象データ
    '''
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
            F[y][x] = a_color
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


F = [
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '#', '_', '_', '_', '#', '#', '_', '_', '_', '#', '_', '#', '_'],
    ['_', '#', '_', '#', '_', '_', '#', '_', '#', '_', '_', '#', '_', '#', '_'],
    ['_', '#', '#', '#', '_', '_', '#', '#', '_', '_', '_', '_', '#', '_', '_'],
    ['_', '#', '_', '#', '_', '_', '#', '_', '#', '_', '_', '_', '#', '_', '_'],
    ['_', '#', '_', '#', '_', '_', '#', '_', '#', '_', '_', '_', '#', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
]
H = 7
W = 15

buckets(F, H, W, 0, 0, '_', ' ')
for f in F:
    print(''.join(f))
