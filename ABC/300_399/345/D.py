N, H, W = [int(l) for l in input().split()]
AB = []
for n in range(N):
    AB.append([int(l) for l in input().split()])

# 全てのタイルが選ばれたかの判定用
allTileSelected = (1 << N) - 1

# マス目データの作成を行います
def makeField(H, W):
    return [0 for h in range(H)]

# すべて埋まったかを判定します
def judge(field, H, W):
    for f in field:
        if f != ((1 << W) - 1):
            return False
    return True

# 該当箇所にタイルを設置できるか判定を行います
def canPut(field, H, W, y, x, dy, dx):
    t = ((1 << dx) - 1) << (W - (x + dx))
    for iy in range(y, y + dy):
        if t & field[iy]:
            return False
    return True

# 該当箇所にタイルの設置を行います
def putTile(field, H, W, y, x, dy, dx):
    t = ((1 << dx) - 1) << (W - (x + dx))
    for iy in range(y, y + dy):
        field[iy] = field[iy] | t

# 該当箇所のタイルの除去を行います
def revertTile(field, H, W, y, x, dy, dx):
    t = ((1 << dx) - 1) << (W - (x + dx))
    for iy in range(y, y + dy):
        field[iy] = field[iy] ^ t

# 空いている箇所を探し，設置可能な場合は設置します
def searchAndPut(field, H, W, dy, dx, t, num):
    for y in range(H-dy+1):
        for x in range(W-dx+1):
            # 空いているマスがある場合
            if not (field[y] & (1 << (W - x - 1))):
                # 設置可能な場合
                if canPut(field, H, W, y, x, dy, dx):
                    # タイルを設置する
                    putTile(field, H, W, y, x, dy, dx)
                    tmp = putTiles(field, H, W, num | t)
                    # 設置完了した場合はTrueを返却する
                    if tmp:
                        return True
                    # 駄目だった場合はタイルを除去する
                    revertTile(field, H, W, y, x, dy, dx)
                return False
    return False

# タイルを置いていきます
def putTiles(field, H, W, num):
    # 揃っているかのチェックを行います
    if judge(field, H, W):
        return True
    # 揃っておらずすべてのタイルを使い切った場合はFalseを返却します
    elif num == allTileSelected:
        return False
    # 各タイルについての走査
    for n in range(N):
        dy, dx = AB[n]
        # 選んだタイルのメモの更新
        t = (1 << n)
        if num & t:
            continue
        # 回転2通り
        for m in range(2):
            if m and dy == dx:
                break
            if m:
                dy, dx = dx, dy
            # タイル設置可能な場合は設置します
            tmp = searchAndPut(field, H, W, dy, dx, t, num)
            # すべて埋めることができた場合はTrueを返却します
            if tmp:
                return True
    return False

# タイル設置可能かの判定を行います
def calc(N, H, W):
    field = makeField(H, W)
    tmp = putTiles(field, H, W, 0)
    return tmp

print("Yes" if calc(N, H, W) else "No")
