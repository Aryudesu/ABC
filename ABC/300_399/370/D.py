from sortedcontainers import SortedSet


def is_in_field(h, w, H, W):
    if h < 0:
        return False
    if h >= H:
        return False
    if w < 0:
        return False
    if w >= W:
        return False
    return True


def xytonum(h, w, H, W):
    """(x, y)から対応する数値に変更する"""
    return h * W + w


def get_break_list(h, w, H, W, Hdata, Wdata, breaked):
    pos = xytonum(h, w, H, W)
    result = []
    if pos in breaked:
        # 壊れてた場合の処理
        # 壊れた列左端のリスト取得
        h_tmp: SortedSet = Hdata.get(h, SortedSet([]))
        idx = h_tmp.bisect_left((w, w))
        left, length = h_tmp[idx]
        right = left + length - 1
        if idx <= w <= right:
            if is_in_field(h, left-1, H, W):
                result.append((h, left - 1))
            if is_in_field(h, right-1, H, W):
                result.append((h, right + 1))
    else:
        # 壊れていない場合の処理
        breaked.add(pos)
        Hdata[h] = SortedSet([(w, w)])
        result.append((h, w))
    print(result)

H, W, Q = [int(l) for l in input().split()]
breaked = set()
Hdata = dict()
Wdata = dict()
for q in range(Q):
    h, w = [int(l) - 1 for l in input().split()]
    get_break_list(h, w, H, W, Hdata, Wdata, breaked)

