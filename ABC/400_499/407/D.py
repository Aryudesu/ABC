def calc(H: int, W: int, h: int, w: int, memo: set, data: list[list[int]], num: int):
    if h == H:
        return num
    new_h = h
    new_w = w + 1
    if new_w == W:
        new_h += 1
        new_w = 0
    result = -1
    now = (h, w)
    # 置けるなら縦に置くパターン
    if h + 1 < H:
        tmp = (h + 1, w)
        if not tmp in memo and not now in memo:
            memo.add(now)
            memo.add(tmp)
            result = max(result, calc(H, W, new_h, new_w, memo, data, num))
            memo.discard(now)
            memo.discard(tmp)
    # 置けるなら横に置くパターン
    if w + 1 < W:
        tmp = (h, w + 1)
        if not tmp in memo and not now in memo:
            memo.add(now)
            memo.add(tmp)
            result = max(result, calc(H, W, new_h, new_w, memo, data, num))
            memo.discard(now)
            memo.discard(tmp)
    # 既に置いてある場合
    if now in memo:
        # 排他的論理和は計算しない
        result = max(result, calc(H, W, new_h, new_w, memo, data, num))
    else:
        # 置いていない場合で置かない場合は排他的論理和は計算する
        result = max(result, calc(H, W, new_h, new_w, memo, data, num^data[h][w]))
    return result


H, W = [int(l) for l in input().split()]
A = []
for h in range(H):
    A.append([int(l) for l in input().split()])
print(calc(H, W, 0, 0, set(), A, 0))
